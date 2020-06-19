import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:5000',
  withCredentials: true
})

const fetchLoggedInStatus = () => http.get('/is-logged-in')

const login = ({ email, password }) => http.post('/login', { email, password })

const getGroups = () => http.get('/groups')

export {
  fetchLoggedInStatus,
  login,
  getGroups
}
