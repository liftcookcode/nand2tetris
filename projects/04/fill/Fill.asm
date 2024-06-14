// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Replace this comment with your code.

@place // starting point
M=0 // place at upper left corner

(LOOP) 
    @KBD 
    D=M 
    @WHITE 
    D;JEQ // if keyboard == 0(aka not pressed) goto White 
    @BLACK 
    0;JMP // otherwise goto Black 

(WHITE)
    @place 
    D=M // put place into D 
    @LOOP 
    D;JLT // jump to LOOP if we are at less than the minimum(0)
    @place 
    D=M 
    @SCREEN 
    A=A+D // calculate place in the screen  
    M=0 // fill the pixel with white 
    @place 
    M=M-1 // decrement place 
    @LOOP 
    0;JMP // jumo to LOOP 

(BLACK)
    @place 
    D=M 
    @8192 // max that place can be 
    D=D-A 
    @LOOP 
    D;JGE // jump to LOOP if we are at the max (place-8192 >= 0)
    @place 
    D=M 
    @SCREEN 
    A=A+D // calculate place 
    M=-1 // fill black 
    @place  
    M=M+1 // increase place by 1 
    @LOOP 
    0;JMP // jump to LOOP if we are at the max (place - 8192 >=0)
    
(END)
@END
0;JMP // infinite loop 

