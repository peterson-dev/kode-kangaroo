/* globals fetch */

const Cookies = require('js-cookie')

function query (selector) {
  return document.querySelector(selector)
}

function queryAll (selector) {
  return document.querySelectorAll(selector)
}

document.addEventListener('DOMContentLoaded', function () {
  for (let form of queryAll('.delete-snippet')) {
    form.addEventListener('submit', function (event) {
      event.preventDefault()
      const csrftoken = Cookies.get('csrftoken')
      fetch(form.action, {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken, 'X-Requested-With': 'XMLHttpRequest' }
      })
        .then(response => {
          if (!response.ok) {
            throw Error(response.statusText)
          }
          query(`#snippet-${form.dataset['snippetpk']}`).remove()
        })
    })
  }
})

// document.addEventListener('DOMContentLoaded', function (event) {
//   const newSnippetForm = query('#new-snippet-form')
//   newSnippetForm.addEventListener('submit', function (event) {
//     event.preventDefault()
//     const csrftoken = Cookies.get('csrftoken')

//     const snippetField = query('#snippet-field')
//     const body = {
//       'snippet': snippetField.value
//     }
//     snippetField.value = ''

//     fetch(newSnippetForm.action, {
//       method: 'POST',
//       headers: {
//         'X-CSRFToken': csrftoken,
//         'X-Requested-With': 'XMLHttpRequest',
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify(body)
//     })
//       .then(response => {
//         if (!response.ok) {
//           throw Error(response.status.Text)
//         }
//         return response.text()
//       })
//       .then(text => {
//         const snippetFragment = document.createRange().createContextualFragment(text)
//         query('#snippet-list').appendChild(snippetFragment)
//       })
//   })
// })
