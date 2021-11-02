# Anipic
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

[![Product Name Screen Shot][product-screenshot]](https://anipic.live)


**Image API**
----
  Returns json data with images.

* **URL**

 ` https://anipic.live/pics/type/category`

* **Types:**

  `sfw`
  `nsfw`

* **Method:**

  `GET`
  
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"count": 1,"next": null,"previous": null,"results": [{"title": "test","image": "https://anipic.live/static/pics/Mugen.jpg"}]}`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Not Found" }`



[![Product Name Screen Shot][product2-screenshot]](https://anipic.live)


**Quote API**
----
  Returns json data with quotes.

* **URL**

  `https://anipic.live/quotes/category`

* **Method:**

  `GET`
  

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"count": 4,"next": null,"previous": null,"results": [{"quote": "Once I’m dead, I won’t even be able to remember you. So I’ll win, no matter what. I’ll live, no matter what!"}]}`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Not Found" }`






## Built With

* Python
* Django
* Postgres
* HTML-CSS-JavaScript
* Bootstrap


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Cosmicoppai/ani_pic.svg?style=for-the-badge
[contributors-url]: https://github.com/Cosmicoppai/ani_pic/contributors
[forks-shield]: https://img.shields.io/github/forks/Cosmicoppai/ani_pic.svg?style=for-the-badge
[forks-url]: https://github.com/Cosmicoppai/ani_pic/network
[stars-shield]: https://img.shields.io/github/stars/Cosmicoppai/ani_pic.svg?style=for-the-badge
[stars-url]: https://github.com/Cosmicoppai/ani_pic/stargazers
[issues-shield]: https://img.shields.io/github/issues/Cosmicoppai/ani_pic.svg?style=for-the-badge
[issues-url]: https://github.com/Cosmicoppai/ani_pic/issues
[license-shield]: https://img.shields.io/github/license/Cosmicoppai/ani_pic.svg?style=for-the-badge
[license-url]: https://github.com/Cosmicoppai/ani_pic/blob/master/LICENSE
[product-screenshot]: https://github.com/Cosmicoppai/ani_pic/blob/master/static/anipic.png
[product2-screenshot]: https://github.com/Cosmicoppai/ani_pic/blob/master/static/anipicquotes.png
