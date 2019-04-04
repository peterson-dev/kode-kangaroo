/* globals fetch, Cookies */
const $ = require('jquery')

// import { format } from "util";


function query (selector) {
  return document.querySelector(selector)
}

document.addEventListener('DOMContentLoaded', function () {
  for (let form of query('.delete-snippet') {
    form.addEventListener('submit', function (event){
        event.preventDefault()
        const csrftoken = Cookies.get('csrftoken')
        fetch(form.action, { 
            method: 'POST' 
            headers: { 'X-CSRFToken': csrftoken, 'X-Requested-With': 'XMLHttpRequest' }
        })
        .then(response => {
          if (!response.ok) {
            throw Error(response.statusText)
          }
          return response.json()
        })
        .then(json => {
          query('#snippet-${form.dataset['title']}').remove()
        })
    })
  }
})

// .then(json => {
//     query('#snippet-${form.dataset['title']}').remove()
//   })

// Working with snippet_list - delete form/button - is the query arg correct? Also need to add unique identifier to the model.