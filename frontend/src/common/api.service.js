// custom CSRF-Tokens with axios
const axios = require("axios")

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export { axios };