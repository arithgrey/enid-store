import moment from 'moment';
export function timePassed(created_at) {

    return moment(created_at).fromNow();

}
