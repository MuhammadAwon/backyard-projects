# 1- Headings

How to give headings in markdown files?

# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

# 2- Block of Words

This is a normal text in MarkDown.

> This is a block of special text
>
> This is a second line

# 3- Line Breaks

This is a 40 days long course of Data Science with Python AKA Python_ka_chilla_with_baba_aammar.

This is a second line.

# 4- Combine Two Things

> ## Block of Words with Heading 2

# 5- Face of Text

**Bold**

*Italic*

***Bold and Italic***

or you can use this symbol _ (underscore)

__Bold__

_Italic_

___Bold and Italic___

# 6- Bullet Points/Lists

* Day-1
* Day-2
* Day-3
* Day-4
* Day-5
  * Day-5a
    * Sub list
* Day-6
* Day-7

 > **Bullet Points using - or +**

* One way

* Another way

> Numbering of lists

 1. Day1
 2. Day2
 3. Day3
 1. Day4
 1. Day5
    1. Day5a
    2. Day5b
 1. Day6
 1. Day7

# 7- Line Breaks or Page Breaks

This is page 1.

---
___
***

This is page 2.

# 8- Links and Hyperlinks

<https://www.youtube.com/c/Codanics>

[The playlist of python ka chilla is here](https://www.youtube.com/playlist?list=PL9XvIvvVL50HVsu-Ao8NBr0UJSO8O6lBI)

[Codanics]: https://www.youtube.com/playlist?list=PL9XvIvvVL50HVsu-Ao8NBr0UJSO8O6lBI

This whole course is [here][Codanics]

# 9- Images and Figures with Link

Codanics is revolutionizing the world of education:
![Logo saved in local directory](logo.png)

Online picture:
![Codanics](https://www.google.com/imgres?imgurl=https%3A%2F%2Fyt3.ggpht.com%2Fytc%2FAKedOLQYkBbgsUZsxjWIF-qyteeEjazqFIxM0h8eatrn%3Ds900-c-k-c0x00ffffff-no-rj&imgrefurl=https%3A%2F%2Fwww.youtube.com%2Fchannel%2FUCmNXJXWONLNF6bdftGY0Otw&tbnid=GRjVtCcWAILqOM&vet=12ahUKEwjM3qGEicD1AhUwAWMBHYM-AfYQMygAegQIARAa..i&docid=rMdsCuD5AJshrM&w=900&h=900&itg=1&q=codanics%20youtube&ved=2ahUKEwjM3qGEicD1AhUwAWMBHYM-AfYQMygAegQIARAa)

**How to Comment in MarkDown?**

> How to comment out a markdown line and its shortcut?

<!---
your comment goes here
-->

[//]: # (your comment goes here)

# 10- Adding Code or Code Block

To write code along with string do this `print("Codanics")`

To write just a block of code then do this:
```print("Codanics")```

> To show the colors of code according Python syntax then write Python with back tick.

```python
x = 5+4
y = 4+1
z = x+y
print(z)
```

# 11- Adding Tables

[//]: # (notice how ":" colon is used for text alignment)
| species | petal_length | sepal_length|
| :------ | :----------: | ----------: |  
| virginica | 18.2 | 19.2 |
| setosa | 15.1 | 17.2 |
| versicolor | 12.2 | 12.2 |
| virginica | 18.2 | 17.2 |
| setosa | 15.1 | 17.2 |
| versicolor | 12.2 | 12.2 |

# 12- Table of Content

[1- Headings](#1--headings)\
[2- Block of Words](#2--block-of-words)\
[3- Line Breaks](#3--line-breaks)\
[4- Combine Two Things](#4--combine-two-things)\
[5- Face of Text](#5--face-of-text)\
[6- Bullet Points/Lists](#6--bullet-pointslists)\
[7- Line Breaks or Page Breaks](#7--line-breaks-or-page-breaks)\
[8- Links and Hyperlinks](#8--links-and-hyperlinks)\
[9- Images and Figures with Link](#9--images-and-figures-with-link)\
[10- Adding Code or Code of Block](#10--adding-code-or-code-block)\
[11- Adding Tables](#11--adding-tables)\
[14- How to Change Color](#14--how-to-change-color)\
[15- Adding Equations in MD](#15--adding-equations-in-md)

# 13- Install Extensions

1. Markdown All in One
2. Markdown PDF
3. markdownlint
4. Markdown Shortcuts
5. vscode-pdf

**Examples using Extensions**

**Bold**

_Italic_

**_Italic and Bold_**

[Codanics MarkDown Tutorial](https://www.youtube.com/watch?v=qJqAXjz-Rh4&list=PL9XvIvvVL50HVsu-Ao8NBr0UJSO8O6lBI&index=22&t=612s)

![Codanics Logo](logo.png)

~~Strikethrough~~

**Add tables**

Column A | Column B | Column C
---------|----------|---------
 A1 | B1 | C1
 A2 | B2 | C2
 A3 | B3 | C3

# 14- How to Change Color

 Example:

> This text color is normal.

<span style="color:green">
This text color is green.
</span>

# 15- Adding equations in MD

> **For In-line math equation**

$this_{is}^{inline}$

> **To add Math Block**

$$
  \int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
$$

For complete instructions visit these documentations: [Math and Equation](https://jupyterbook.org/content/math.html), [MathJax docs](http://docs.mathjax.org/en/latest/).
