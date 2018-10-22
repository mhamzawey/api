import React  from 'react';
import Modal from 'react-modal';

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
    render() {
        const rows = [];
        this.props._events.forEach((event) => {
            rows.push(<EventRow event={event} key={`event-${event.id}`}/>
            );
        });

        return (
            <div style={{padding:"30px"}}>
                <div className="row" style={{justifyContent:"center"}}>
                    <h1 style={{textAlign:"center"}}>Daila Calendar</h1>
                </div>

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
