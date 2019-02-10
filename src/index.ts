import * as express from 'express';
import * as bodyParser from 'body-parser';
import * as fs from 'fs';
import * as child_process from 'child_process';
import { init} from './websocket';
import 'source-map-support/register'

const app = express()

// you explicitly create the http server
var server = require('http').createServer(app);
init(server);
server.listen(3000);


interface Ticket {
  id?: number;
  bags: string;
  class: string;
  firstname: string;
  lastname: string;
  phone: string;
  priority: string;
  seat: string;
}

interface BoardingPass {
  id?: number;
  ticketID: number;
  groupNumber: string;
  seatNumber: string;
}

interface BoardingStatus {
  seat: string;
  pass: BoardingPass;
  boarded: boolean;
}


const tickets: Ticket[] = [];

const boardingPasses: BoardingPass[] = [];

const boardingStatuses: BoardingStatus[] = [];


app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});
app.use(bodyParser.json());
app.use((req, res, next) => {
  console.log(req.path);
  console.log(req.query);
  next();
});



app.post('/ticket', (req, res) => {
  const ticket: Ticket = req.body;
  console.log(req.body)
  ticket.id = tickets.length + 1;
  tickets.push(ticket);
  res.send(JSON.stringify({ 'ticketID': ticket.id }));
})

// Type guard
// function isTicket(obj: any): Ticket {
//   if (!obj.firstName) throw new Error('missing first name');
//   if (!obj.lastName) throw new Error('missing last name');
//   return obj as Ticket;
// }

app.get('/tickets', (req, res) => {
  res.send(tickets);
});

app.get('/ticket', (req, res) => {
  const ticket = tickets.find((ticket) => ticket.id == req.query.id);
  if (!ticket) {
    res.statusCode = 404;
    res.send(JSON.stringify({ 'Error': 'ticket not found!' }));
    return;
  }
  console.log(ticket);
  res.send(ticket);

});

app.get('/boardingpass', (req, res) => {
  const pass = boardingPasses.find((pass) => pass.ticketID == req.query.id)
  if (!pass) {
    res.statusCode = 404;
    res.send(JSON.stringify({ 'Error': 'pass not found!' }));
    return;
  }
  res.send(pass);
})

app.post('/boarding', (req, res) => {
  //write the tickets to a json file


  const strTix = JSON.stringify(tickets);
  fs.writeFileSync('passenger_List.json', strTix, 'utf8');

  let numOfPriorityPeople = 0;

  for (let ticket of tickets) {
    if (ticket.priority) {
      numOfPriorityPeople = numOfPriorityPeople + 1;
    }
  }

  const steffenv6Args = ['steffenv6.py', '33', '5', numOfPriorityPeople.toString(), '0.75'];
  const manifestArgs = ['manifestlogic.py', 'passenger_List.json', 'seat_status.json', 'boarding_groups.json'];
  child_process.spawnSync("python", steffenv6Args);
  child_process.spawnSync("python", manifestArgs);

  const seatAssignments: { passenger: number, number: string }[] = JSON.parse(fs.readFileSync("manifest.json", "utf8"));
  console.log(seatAssignments);

  const boardingGroups: {
    [index: string]: string[]
  } = JSON.parse(fs.readFileSync('boarding_groups.json', 'utf8'));
  console.log(boardingGroups);

  //call script
  //construct boardingPasses and boardingStatuses
  for (let ticket of tickets) {

    const assignment = seatAssignments.find(passenger => ticket.id ? (passenger.passenger == ticket.id) : false);
    if (!assignment) continue;

    for (let group in boardingGroups) {
      if (group === 'bagged' || group === 'nobagged') continue;

      const groupSeats = boardingGroups[group];
      const seat = groupSeats.find(groupSeat => groupSeat === assignment.number);
      if (!seat) continue;

      const boardingPass: BoardingPass = {
        seatNumber: assignment.number,
        groupNumber: group,
        ticketID: ticket.id!,
        id: boardingPasses.length + 1

      }

      boardingPasses.push(boardingPass);

      const boardingStat: BoardingStatus = {
        seat: assignment.number,
        pass: boardingPass,
        boarded: false
      }

      boardingStatuses.push(boardingStat);

      break;

    }
  }

  res.sendStatus(200);
})

app.post('/board', (req, res) => {

  if (req.body.id === '1000') {
    res.sendStatus(200);
    return;
  }
  parseInt(req.body.id)
  const pass = boardingStatuses.find((pass) => {
    console.log(pass.pass.id, parseInt(req.body.id))
    return pass.pass.id == parseInt(req.body.id)
  })
  if (!pass) {
    res.statusCode = 404;
    res.send(JSON.stringify({ 'Error': 'pass not found!' }));
    return;
  }

  pass.boarded = true;
  console.log(boardingStatuses);
  res.sendStatus(200);

})

app.get('/stats', (req, res) => {
  res.send(boardingStatuses);
});

app.post('/clear', (req, res) => {
  tickets.length = 0;
  boardingPasses.length = 0;
  boardingStatuses.length = 0;
  res.sendStatus(200);
})



console.log('**ready**');