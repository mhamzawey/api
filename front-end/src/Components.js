import React, { Component } from 'react';

export class EventRow extends React.Component {
    render() {
        const event = this.props.event;

        return (
            <tr>
                <td>event.title</td>
                <td>{event.description}</td>
            </tr>
        );
    }
}

export class EventTable extends React.Component {
    render() {
        const rows = [];
        let lastCategory = null;

        this.props._events.forEach((event) => {
            rows.push(<EventRow event={event}/>
            );
        });

        return (
            <table>
                <thead>
                <tr>
                    <th>Title</th>
                    <th>Description</th>
                </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
        );
    }
}
