import * as http from 'http';
import { UniversalWebSocketServer } from 'universal-ws-server';

let connections: any = [];
let WebSocketServer: UniversalWebSocketServer;
export function init(httpServer: http.Server) {
    WebSocketServer = new UniversalWebSocketServer(httpServer);
    WebSocketServer.on('connected', (connection: any) => {
        console.log('Successfully connected to a client!');
        connections.push(connection);
    });
    WebSocketServer.on('close', (connection: any) => {
        console.log('Client no longer connected!');
        connections = connections.filter(function (ele: any) {
            return ele != connection;
        });
    });
}

export function boarded(ticket: string, bag?: boolean) {
    console.log('boarded!');
    connections.forEach((connection: any) => {
        console.log('sending!');
        WebSocketServer.send(connection, 'board', { number: ticket, bag: bag });
    });
}

setInterval(() => {
    boarded('16:A', true);
}, 1000);
