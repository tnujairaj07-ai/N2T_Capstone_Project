// Benchmark test for Pong
   @256
   D=A
   @SP
   M=D
   @133
   0;JMP
(LABEL_INIT)
   @SP
   A=M
   M=D
   @SP
   M=M+1
   @RET_ADDR_0
   D=A
   @LABEL_INIT
   0;JMP
(RET_ADDR_0)
   @R0
   D=M
   @R1
   D=D+M
   @R2
   M=D
(PONG_LOOP)
   @KBD
   D=M
   @PONG_LOOP
   D;JEQ
(END)
   @END
   0;JMP

   