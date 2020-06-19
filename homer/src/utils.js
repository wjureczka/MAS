import { fetchLoggedInStatus } from './api'

const authGuard = (to, from, next) => {
  fetchLoggedInStatus()
    .then(() => next())
    .catch(() => next('/login'))
}

export {
  authGuard
}
