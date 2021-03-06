# Hobbytronics TFT - driver library constants
# Author: Philip Howard <phil@gadgetoid.com>
# Version: 1.0

CMD_BEGIN			= chr(27)
CMD_END				= chr(255)
RETURN				= chr(13)

CMD_CLEAR			= chr(0)
CMD_FG_COLOR		= chr(1)
CMD_BG_COLOR		= chr(2)
CMD_SCREEN_ROTATION	= chr(3)
CMD_FONT_SIZE		= chr(4)
CMD_LINE_START		= chr(5)
CMD_POS_TEXT		= chr(6)
CMD_POS_PIXEL		= chr(7)
CMD_DRAW_LINE		= chr(8)
CMD_DRAW_BOX		= chr(9)
CMD_DRAW_FILLED_BOX = chr(10)
CMD_DRAW_CIRCLE		= chr(11)
CMD_DRAW_FILLED_CIRCLE	= chr(12)
CMD_DISPLAY_BITMAP	= chr(13)
CMD_BRIGHTNESS		= chr(14)
CMD_SET_COLOR		= chr(15)
CMD_DRAW_PIXL		= chr(16)

LINE_BEGINNING		= CMD_BEGIN + CMD_LINE_START + CMD_END
TEXT_BEGINNING 		= CMD_BEGIN + CMD_POS_TEXT + chr(0) + chr(0) + CMD_END

CLEAR_SCREEN		= CMD_BEGIN + chr(0) + CMD_END

SCREEN_WIDTH		= 160
SCREEN_HEIGHT		= 128

SCREEN_WIDTH_HALF	= SCREEN_WIDTH/2
SCREEN_HEIGHT_HALF	= SCREEN_HEIGHT/2

# Built-in colours
COL_BLACK	= 0
COL_BLUE	= 1
COL_RED		= 2
COL_GREEN	= 3
COL_CYAN	= 4
COL_MAGENTA	= 5
COL_YELLOW	= 6
COL_WHITE	= 7

# User-customisable colour-values
COL_USER_1	= 8
COL_USER_2	= 9
COL_USER_3	= 10
COL_USER_4	= 11
COL_USER_5	= 12
COL_USER_6	= 13
COL_USER_7	= 14
COL_USER_8	= 15

# Redundant shorthand for BG/FG colour commands
BG_COL_BLACK	= CMD_BEGIN + chr(2) + chr(0) + CMD_END
BG_COL_BLUE		= CMD_BEGIN + chr(2) + chr(1) + CMD_END
BG_COL_RED		= CMD_BEGIN + chr(2) + chr(2) + CMD_END
BG_COL_GREEN	= CMD_BEGIN + chr(2) + chr(3) + CMD_END
BG_COL_CYAN		= CMD_BEGIN + chr(2) + chr(4) + CMD_END
BG_COL_MAGENTA	= CMD_BEGIN + chr(2) + chr(5) + CMD_END
BG_COL_YELLOW	= CMD_BEGIN + chr(2) + chr(6) + CMD_END
BG_COL_WHITE	= CMD_BEGIN + chr(2) + chr(7) + CMD_END

FG_COL_BLACK	= CMD_BEGIN + chr(1) + chr(0) + CMD_END
FG_COL_BLUE		= CMD_BEGIN + chr(1) + chr(1) + CMD_END
FG_COL_RED		= CMD_BEGIN + chr(1) + chr(2) + CMD_END
FG_COL_GREEN	= CMD_BEGIN + chr(1) + chr(3) + CMD_END
FG_COL_CYAN		= CMD_BEGIN + chr(1) + chr(4) + CMD_END
FG_COL_MAGENTA	= CMD_BEGIN + chr(1) + chr(5) + CMD_END
FG_COL_YELLOW	= CMD_BEGIN + chr(1) + chr(6) + CMD_END
FG_COL_WHITE	= CMD_BEGIN + chr(1) + chr(7) + CMD_END
