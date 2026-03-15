export class cookieUtils {
  setItemInCookie(name, value, duration = 60000) {
    document.cookie = `${name}=${value}; path=/; max-age=${duration *60000}`//a minute in millisecond is 60,000 so we will multiple the duration by the minute eg. 60*60,000 = 1 hour
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
export function onUpdate(callback, iteration_rate) {
  try {
    const updateInterval = setInterval(callback, iteration_rate || 500)
  } catch (e) {
    throw new Error('An error occured @ onUpdated function' + e)
  }
};
