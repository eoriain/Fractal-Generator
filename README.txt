Assignment 1 - Turtle Fractal Generator
Eoghan O Riain - 111319036 

This Turtle Generator was developed using Python 3.9.7. Please note that other Python versions may produce varied graphical results.

The purpose of my Turtle Generator is to allow the user full artistic control over the turtle graphic generation. There are two main panels which occupy the space of Turtle Generator: 
The Control Panel and The Canvas Frame.


The Control Panel:
The control panel is broken in 6-sections to allow the user to specify their turtle parameters in varies form input method (i.e. scale bar, data entry, option menu etc.). This is where creative control is handed over to the user. Below is a breakdown of each of the 6-sections of the control panel:

Length & Order:
This requires the user to enter specific dimensions they would like the turtle to draw too. The length value will represent the length of the first recursion of the fractal image.  The order represents the the number of recursions that will occur for the specified fractal.
 
Fractal Type Selection:
12 fractals have been designed and included within the Turtle Generator. In order to review the list of fractals and make their selection, the user has been given a drop-down menu (or option menu) with all fractal include so the user can take their pick. Below is a list of the fractals that were my personal contributions to this list:


- Octahedron
This is the first of my personal contributions to the selection of fractals. The octahedron is a complex fractal that is 3D in nature which posed a challenge in programming the turtle representation. An octahedron is an 8-sided 3D object with triangular faces and I am satisfied with its representation in 2D space.

- Pentagon (without spacing)
The pentagon fractal was discussed in class and the question was posed how the pentagons could be shown without spacing. This was achieved by calculating the Cos(72 degrees) to determine the adjacent length of the angle. This gave us a factor of 0.3819660114*L.

- Circle
This is my personal circle fractal. Within the parent circle the are 4 smaller circles that fit flush against eachother. The radius required for these circles we calculated using Rbig = Rsmall + sqrt(2). With this equation, I determined that the remaining spaces between these 4 circles could be occupied by even smaller circles with radius sprt(2).

Pen Speed & Pen Width Scalers:
The speed at which the pen completes the process of drawing the fractal is referred to as the “Pen Speed”. The values associated with the speed of the pen operate a little bit differently than just from slowest to fastest. For pen speed, “0” is the fastest and “1” is the slowest. The speed of the pen then scales up to its second fastest point, “10”.
The pen width is a little more straight forward. This represents the thickness of the pen line as it is drawn on the canvas. This ranges from its thinest value “1” to its thickest value “10”.
The most user friendly approach to include this functionality whilst maintaining the maximum and minimum limits  of the speed and width was to represent them as scale bars (or sliders).

Turtle Shape:
Users have the option to select between 6 turtle shapes to represent the pen motion. The turtle shapes included are the classic icon, an arrow, a square, a circle, a triangle and a turtle.		

Pen & Canvas Colour Picker:
When selected, the user will be presented with a colour dialog box in which the full spectrum of colours can be selected from to represent the turtle colour or the canvas colour. If a colour has not been selected for the turtle or the canvas, they will remain in their default colours of a white canvas and a black turtle.
Please note, the colour of the pen can be changed while the fractal is being drawn. This gives the user the ability to create a multi-colour fractal for higher-order fractals.

Draw & Reset Functions:
Draw - Once selected the turtle will begin to construct the fractal of choice to the user’s specification. As previously mentioned, the turtle will not if either the length or the order has not been given a value.
Reset - Once an image has been completed by the turtle. The user can press the “Reset” button to the control panel and canvas frame back their default setting and values.
Both buttons have an additional function associated with them that will change the colour of the text on the button and underline the text when the cursor is over the button.


The Canvas Frame
The canvas frame contains the graphical window, in which the user customised fractal will be drawn and displayed. As well as the graphical window, the canvas frame also houses the fractal information panel. When a fractal is selected from the option menu and it is given its length and order, a short paragraph of information relating to the selected fractal will appear in the fractal information panel once the draw button is clicked. The fractal information panel will also pull through and display the length and order that has been selected by the user.
