import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:5000',
  withCredentials: true
})

const fetchLoggedInStatus = () => http.get('/is-logged-in')

const login = ({ email, password }) => http.post('/login', { email, password })

const getGroups = () => http.get('/groups')

const postNewGroup = ({
  // eslint-disable-next-line camelcase
  group_name,
  // eslint-disable-next-line camelcase
  preferred_locations,
  // eslint-disable-next-line camelcase
  preferred_room_quantity,
  // eslint-disable-next-line camelcase
  preferred_size,
  // eslint-disable-next-line camelcase
  preferred_budget
}) => http.post('/groups', {
  group_name,
  preferred_locations,
  preferred_room_quantity,
  preferred_size,
  preferred_budget
})

const postNewUserToGroup = ({ groupId, email }) => http.post(`/groups/${groupId}/add-user`, { email })

export {
  fetchLoggedInStatus,
  login,
  getGroups,
  postNewGroup,
  postNewUserToGroup
}
