# julia_gen
A Julia Set Fractal Generator for Windows and Linux

I. Basic Functions
This tool is intended as a comprehensive suite of math and color to help artists, computer scientists, and mathematicians explore the beautiful world of fractals with one of the most common and simple fractals known as the Julia Set. With this tool, you can generate Julia Set fractals using either polynomial, exponential, or trig functions and edit your images with different colors, sizes, and ranges.

To get started, try out the default settings and just hit “Generate” when you start the program!

The function that created this image is popular among Julia set fanatics; just a simple parabola f(z)=z^2 + c. Now the most interesting part of a Julia set is actually that number c. C is a complex number whose default value (which generated the above picture) is 0.285+0.01i. Change this number (maybe try 0.288+0.006i) just a little and generate again. Now you’ve got something completely different! How did that happen? How did such a small change make something so different? What you’re marveling right now is a product of the butterfly effect. This is because fractals are intimately connected to concepts in chaos theory. But for now, let’s learn to move the damn thing around to explore!

Let's try another experiment. Go back to the function we started with and generate it again. Let's try to zoom in on that pretty spiral on the bottom left. First set the zoom at 0.5, vertical shift to -0.45 and horizontal shift to 0.20. This will pretty much center you on the spiral. Now to zoom in, lower the range the fractal is plotted over, down to 0.25, and smaller still (you may need to shift left and right as you do this)! After doing this a few times, you'll notice you're starting to repeat yourself. This is a second amazing property of fractals: self-similarity. No matter which part we zoom in on, we will always get something similar (but not exactly) the whole. This part takes practice and trial and error so don't fret if it takes some getting used to!

a. Choosing a Function

Polynomials are the classic functions to choose for Julia Sets because they are simple and yet generate beautifully complex images. You can probably find infinite fun just by changing the seed c little by little. But I don’t believe in limiting you! The dropdown menu enables you to access a bunch of functions which work with complex numbers including trigonometric functions, logarithms, exponentials, and hyperbolic. In addition, you can raise these functions to a power n (supports negative exponents) or multiply them by q.

If you’re not sure where to start, try some of these! 
F(z) = z^2 + (1-phi), phi is the golden ratio: 1.618…
F(z) = z^2 + (-0.8 + 0.156i)
F(z) = z^2 + (0 - 0.8i)
F(z) = z^2 + (-0.7269 + 0.1889i)
F(z) = z^3 + (0.666 + 0.666i)
F(z) = z^3 + (0.333 + 0.711i)
F(z) = z^4+ (-0.484)
F(z) = 1/(z^-2) + (0.439 + 0.347i)
F(z) = sin(z)^2 + (0.420 + 0.180i)
F(z) = cosh(z) + (-0.510)
F(z) = exp^(-z^2) + (-0.404 - 0.686i)
F(z) = exp(-z^2)^2+(-0.721+0.207i)


b. Color Schemes

The images in this program are generated based on a function performed on RGB values (specfically x%m1*m2 where x is the output of the julia set generator function and m1 and m2 are distinct factors of 256 excluding 1 2 128 and 256 where m1*m2 = 256) and a black and white theme yielding 61 schemes. Each pixel can be thought of as an input (an x-value) to our function and is colored based on how quickly the function tends to infinity. The more times your function can act on itself without blowing up, the farther away you get from the background color. You can also adjust the horizontal range the function is plotted on (-1.2 to 1.2 is the default, -2 to 2 is the max since fractals get boring outside of this range). Enter smaller numbers to zoom in, larger ones to zoom out

c. Saving an Image

Fractals are automatically displayed on a 500x500 plane when you hit generate, but can also be saved in a resolution of your choice. Change the values of resolution, then click “Save Image” to save as a jpg, png, or xpm.

II. Bug Reports and Contact

Before anything, if you have any problems make sure that the program the ui file, and other files are in the same folder as you downloaded them!

This software was created using PyQt4 and Qt4 Designer with the python module numpy. This project is open-source and available at https://github.com/mjfernez/julia_gen under a GNU GPL License. Please direct comments and complaints here. Currently I am working to write a full introduction to fractals using this tool, but I need to make sure the details are right and I credit everyone correctly so bear with me! I am also considering adding functionality for more complex polynomials like (z^2+z-1) or (1-z^3)/(1-z^4), though the formatting will require me to redraft this program. I may release a separate tool for this since this program is really aimed for people without a knowledge of fractals, but if you have any clever ideas contact me.

III. Special Thanks
To Rosetta Code for their repository of Julia Set programs https://rosettacode.org/wiki/Julia_set#Python
To Wikipedia for their list of Julia sets, detailed explanation, and generally giving me an education where school failed

--MJF
