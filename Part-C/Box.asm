(LOOP)
    @KBD
    D=M
    @DRAW
    D;JNE

(CLEAR)
    @color
    M=0
    @RENDER
    0;JMP

(DRAW)
    @color
    M=-1

(RENDER)
    @20
    D=A
    @row_count
    M=D

    @16768
    D=A
    @cur_addr
    M=D

(ROW_LOOP)
    @row_count
    D=M
    @LOOP
    D;JEQ

    @1
    D=A
    @col_count
    M=D

(COL_LOOP)
    @col_count
    D=M
    @NEXT_ROW
    D;JEQ

    @color
    D=M
    @cur_addr
    A=M
    M=D

    @cur_addr
    M=M+1
    @col_count
    M=M-1
    @COL_LOOP
    0;JMP

(NEXT_ROW)
    @32
    D=A
    @1
    D=D-A

    @cur_addr
    M=D+M

    @row_count
    M=M-1
    @ROW_LOOP
    0;JMP