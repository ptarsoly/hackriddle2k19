import * as express from 'express';
import * as bodyParser from 'body-parser';
import 'source-map-support/register'

const app = express()

// declare function create(o: object | null): void;

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
  groupNumber: number;
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
  ticket.id = tickets.length;
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

app.post('/boardingPass', (req, res) => {
  const pass = boardingPasses.find((pass) => pass.ticketID == req.body.ticketID)
  if(!pass) {
    res.statusCode = 404;
    res.send(JSON.stringify({ 'Error': 'pass not found!' }));
    return;
  }
  res.send(pass);
})

app.get('/boarding', (req, res) => {
  //call script
  //construct boardingPasses and boardingStatuses
  // for(ticket of tickets) {
  //   const boardingPass: BoardingPass;
  //   boardingPass.
  //   boardingPasses.push()
  // }
})

app.post('/board', (req, res) => {

  const pass = boardingStatuses.find((pass) => pass.pass.id == req.body.id)
  if(!pass) {
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

})

app.listen(3000);

console.log('**ready**');