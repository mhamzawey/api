import React  from 'react';
import Modal from 'react-modal';
import {getSeachEvent} from "./api";

Modal.setAppElement('#root')

export class EventRow extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            modalIsOpen: false
        };
        this.openModal = this.openModal.bind(this);
        this.afterOpenModal = this.afterOpenModal.bind(this);
        this.closeModal = this.closeModal.bind(this);
    }
    openModal() {
        this.setState({modalIsOpen: true});
    }

    afterOpenModal() {
        // references are now sync'd and can be accessed.
    }

    closeModal() {
        this.setState({modalIsOpen: false});
    }

    render() {
        const event = this.props.event;

        return (

            <tr>
                <Modal
                    isOpen={this.state.modalIsOpen}
                    onAfterOpen={this.afterOpenModal}
                    onRequestClose={this.closeModal}
                    style={{

                        content: {
                            width: '35%',
                            height:'50%',
                            margin: 'auto',

                        }
                    }}
                    contentLabel="Example Modal"
                >
                    <h2 style={{textAlign:"center"}}>{event.description}</h2>
                </Modal>

                <td onClick={this.openModal}>{event.title}</td>
                <td>{event.category}</td>
                <td>{event.start_date}</td>
                <td>{event.end_date}</td>


            </tr>
        );
    }
}


export class EventTable extends React.Component {
    constructor(props) {
        super(props);
    }
    state = {
        query: '',
        _events: this.props._events
    };

    handleInputChange = () => {

        if (this.search.value.length >=3){

            getSeachEvent(this.search.value).then(res => this.setState({_events:res.data.results}))
                .catch(err => alert("An error occurred"));
        }else{
            this.setState({_events:this.props._events})
        }


    };
    render() {
        const rows = [];
        this.state._events.forEach((event) => {
            rows.push(<EventRow event={event} key={`event-${event.id}`}/>
            );
        });

        return (
            <div style={{padding:"30px"}}>
                <div className="row" style={{justifyContent:"center"}}>
                    <h1 style={{textAlign:"center"}}>Daila Calendar</h1>
                </div>
                <div className="fa-search row" style={{justifyContent:"center"}}>
                    <form>
                        <input
                            placeholder="Search for..."
                            style={{textAlign:"center",width:"400px"}}
                            ref={input => this.search = input}
                            onChange={this.handleInputChange}
                        />

                    </form>
                </div>
                <br/>

                <table className="table table-striped table-bordered">
                    <thead>
                    <tr>
                        <th scope="row">Title</th>
                        <th scope="row">Category</th>
                        <th scope="row">Start Date</th>
                        <th scope="row">End Date</th>
                    </tr>
                    </thead>
                    <tbody>{rows}</tbody>
                </table>
            </div>
        );
    }
}

