import React, { Component } from 'react';
import './App.css';
import {getEvents} from "./api";
import {EventTable} from "./Components";
class App extends Component {

    constructor(props) {
        super(props);
        this.state = {
            _events: null
        };

        getEvents().then(res => this.setState({_events:res.data.results}))
            .catch(err => alert("An error occurred"));

    }



    render() {
        if(!this.state._events){
            return null
        }
        else{
            console.log(this.state._events);
            return (
                <EventTable _events={this.state._events} />
            );
        }

    }
}

export default App;
