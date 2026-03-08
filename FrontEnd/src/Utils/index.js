export class cookieUtils {
  setItemInCookie(name, value, duration = 86400000) {
    document.cookie = `${name}=${value}; path=/; max-age=${duration}`
    return true
  }
  getFromCookie(name) {
    const cookies = document.cookie.split(';')
    for (let cookie of cookies) {
      const [cookieName, cookieValue] = cookie.trim().split('=')
      if (cookieName === name) {
        return cookieValue
      }
    }
    return null
  }
}
export class storageUtils {
  setItemInLocal(name, value) {
    if (typeof name !== 'string') {
      throw new Error('Name and value must be strings')
    }
    window.localStorage.setItem(name, value)
    return true
  }
  getItemInLocal(name) {
    if (typeof name !== 'string') {
      throw new Error('Name must be strings')
    }
    return window.localStorage.getItem(name)
  }
  setItemInSession(name, value) {
    if (typeof name !== 'string') {
      throw new Error('Name and value must be strings')
    }
    window.sessionStorage.setItem(name, value)
    return true
  }
  getItemInSession(name) {
    if (typeof name !== 'string') {
      throw new Error('Name must be strings')
    }
    return window.sessionStorage.getItem(name)
  }
}
