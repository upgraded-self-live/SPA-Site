export class cookieUtils {
  setItemInCookie(name, value, duration = 60000) {
    const encoddedValue = encodeURIComponent(value)
    document.cookie = `${name}=${encoddedValue}; path=/; max-age=${duration * 6000}` //a minute in millisecond is 60,000 so we will multiple the duration by the minute eg. 60*60,000 = 1 hour
    return true
  }
  getFromCookie(name) {
    const cookies = document.cookie.split(';')
    for (let cookie of cookies) {
      const [cookieName, cookieValue] = cookie.trim().split('=')
      if (cookieName === name) {
        return decodeURIComponent(cookieValue) //remove all automatic query types ":" = "$" or smth else idk; if there is any
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
  let errorIteration, lastError
  try {
    const updateInterval = setInterval(callback, iteration_rate || 500)
  } catch (e) {
    throw new Error('An error occured @ onUpdated function, cancelling function' + e)
    if (errorIteration > 5) {
      //check how many error we get and cancel the interval if the error persists
      clearInterval(updateInterval)
    }
    if (String(e) === String(lastError)) {
      errorIteration++
    } else {
      errorIteration = 0
    }
    lastError = e
  }
}
//Due to pattern recignition, IsMob function was created to stop repition of checking for mobile in each component
export function isMob() {
  onUpdate(() => {
    if (window.innerWidth <= 820) {
      return true
    } else {
      return false
    }
  }, 5)
}
//This function will loop through an argument array then allocated the values if false to their respective index on another array
export class arrayProperties {
  constructor(objs) {
    this.object = objs
    console.log(this.object)
  }
  ifFalse(placeHolderObjMap) {
    const objToArray = Object.keys(this.object) //Converts object to array
    objToArray.forEach((key) => {
      //loops through the array of keys
      if (this.object[key] === undefined) {
        //if the object at index of key is undefined
        this.object[key] = placeHolderObjMap[key] //set the indexed object to the same index in that array
        //key is a list of indices with their values allocated to it
        console.log(`${this.object[key]}:${placeHolderObjMap[key]}`)
      }
    })
  }
  ifTrue(trueArray) {
     const objToArray = Object.keys(this.object) //Converts object to array
     objToArray.forEach((key) => {
       //loops through the array of keys
       if (this.object[key]) {
         //if the object at index of key is undefined
         this.object[key] = placeHolderObjMap[key] //set the indexed object to the same index in that array
         //key is a list of indices with their values allocated to it
         console.log(`${this.object[key]}:${placeHolderObjMap[key]}`)
       }
     })
  }
}
