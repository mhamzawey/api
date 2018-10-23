import axios from 'axios'

export  const BASE_URL = "http://localhost:4000";
export const events_url = "/events/";


export const getEvents = () => {
    return new Promise((resolve, reject) => {
        return axios.get(BASE_URL+events_url)
            .then((res) => resolve(res));
    })
    .catch(err => console.log(err));
};

export const getSeachEvent = (searchterm) => {
    return new Promise((resolve, reject) => {
        return axios.get(BASE_URL+events_url+"?search="+searchterm)
            .then((res) => resolve(res));
    })
        .catch(err => console.log(err));
};

