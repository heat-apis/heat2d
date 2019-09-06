import pygame

key_dictionary = {
                  "backspace" : pygame.K_BACKSPACE,
                  "tab" : pygame.K_TAB ,
                  "clear" : pygame.K_CLEAR,
                  "return" : pygame.K_RETURN,
                  "pause" : pygame.K_PAUSE,
                  "escape" : pygame.K_ESCAPE,
                  "space" : pygame.K_SPACE,
                  "exclaim" : pygame.K_EXCLAIM,
                  "quotedbl" : pygame.K_QUOTEDBL,
                  "hash" : pygame.K_HASH,
                  "dollar" : pygame.K_DOLLAR,
                  "ampersand" : pygame.K_AMPERSAND,
                  "quote" : pygame.K_QUOTE,
                  "lparen" : pygame.K_LEFTPAREN,
                  "rparen" : pygame.K_RIGHTPAREN,
                  "asterisk" : pygame.K_ASTERISK,
                  "plus" : pygame.K_PLUS,
                  "comma" : pygame.K_COMMA,
                  "minus" : pygame.K_MINUS,
                  "period" : pygame.K_PERIOD,
                  "slash" : pygame.K_SLASH,
                  "0" : pygame.K_0,
                  "1" : pygame.K_1,
                  "2" : pygame.K_2,
                  "3" : pygame.K_3,
                  "4" : pygame.K_4,
                  "5" : pygame.K_5,
                  "6" : pygame.K_6,
                  "7" : pygame.K_7,
                  "8" : pygame.K_8,
                  "9" : pygame.K_9,
                  "colon" : pygame.K_COLON,
                  "semicolon" : pygame.K_SEMICOLON,
                  "less" : pygame.K_LESS,
                  "equals" : pygame.K_EQUALS,
                  "greater" : pygame.K_GREATER,
                  "question" : pygame.K_QUESTION,
                  "at" : pygame.K_AT,
                  "leftbracket" : pygame.K_LEFTBRACKET,
                  "backslash" : pygame.K_BACKSLASH,
                  "rightbracet" : pygame.K_RIGHTBRACKET,
                  "caret" : pygame.K_CARET,
                  "underscore" : pygame.K_UNDERSCORE,
                  "backquote" : pygame.K_BACKQUOTE,
                  "a" : pygame.K_a,
                  "b" : pygame.K_b,
                  "c" : pygame.K_c,
                  "d" : pygame.K_d,
                  "e" : pygame.K_e,
                  "f" : pygame.K_f,
                  "g" : pygame.K_g,
                  "h" : pygame.K_h,
                  "i" : pygame.K_i,
                  "j" : pygame.K_j,
                  "k" : pygame.K_k,
                  "l" : pygame.K_l,
                  "m" : pygame.K_m,
                  "n" : pygame.K_n,
                  "o" : pygame.K_o,
                  "p" : pygame.K_p,
                  "q" : pygame.K_q,
                  "r" : pygame.K_r,
                  "s" : pygame.K_s,
                  "t" : pygame.K_t,
                  "u" : pygame.K_u,
                  "v" : pygame.K_v,
                  "w" : pygame.K_w,
                  "x" : pygame.K_x,
                  "y" : pygame.K_y,
                  "z" : pygame.K_z,
                  "delete" : pygame.K_DELETE,
                  #Numpad numbers
                  "n0" : pygame.K_KP0,
                  "n1" : pygame.K_KP1,
                  "n2" : pygame.K_KP2,
                  "n3" : pygame.K_KP3,
                  "n4" : pygame.K_KP4,
                  "n5" : pygame.K_KP5,
                  "n6" : pygame.K_KP6,
                  "n7" : pygame.K_KP7,
                  "n8" : pygame.K_KP8,
                  "n9" : pygame.K_KP9,
                  "nperiod" : pygame.K_KP_PERIOD,
                  "divide" : pygame.K_KP_DIVIDE,
                  "multiply" : pygame.K_KP_MULTIPLY,
                  "nminus" : pygame.K_KP_MINUS,
                  "nplus" : pygame.K_KP_PLUS,
                  "enter" : pygame.K_KP_ENTER,
                  "nequals" : pygame.K_KP_EQUALS,
                  "up" : pygame.K_UP,
                  "down" : pygame.K_DOWN,
                  "right" : pygame.K_RIGHT,
                  "left" : pygame.K_LEFT,
                  "insert" : pygame.K_INSERT,
                  "home" : pygame.K_HOME,
                  "end" : pygame.K_END,
                  "pageup" : pygame.K_PAGEUP,
                  "pagedown" : pygame.K_PAGEDOWN,
                  "f1" : pygame.K_F1,
                  "f2" : pygame.K_F2,
                  "f3" : pygame.K_F3,
                  "f4" : pygame.K_F4,
                  "f5" : pygame.K_F5,
                  "f6" : pygame.K_F6,
                  "f7" : pygame.K_F7,
                  "f8" : pygame.K_F8,
                  "f9" : pygame.K_F9,
                  "f10" : pygame.K_F10,
                  "f11" : pygame.K_F11,
                  "f12" : pygame.K_F12,
                  "f13" : pygame.K_F13,
                  "f14" : pygame.K_F14,
                  "f15" : pygame.K_F15,
                  "numlock" : pygame.K_NUMLOCK,
                  "capslock" : pygame.K_CAPSLOCK,
                  "scrollock" : pygame.K_SCROLLOCK,
                  "rshift" : pygame.K_RSHIFT,
                  "lshift" : pygame.K_LSHIFT,
                  "rctrl" : pygame.K_RCTRL,
                  "lctrl" : pygame.K_LCTRL,
                  "ralt" : pygame.K_RALT,
                  "lalt" : pygame.K_LALT,
                  "rmeta" : pygame.K_RMETA,
                  "lmeta" : pygame.K_LMETA,
                  "lsuper" : pygame.K_LSUPER,
                  "rsuper" : pygame.K_RSUPER,
                  "mode" : pygame.K_MODE,
                  "help" : pygame.K_HELP,
                  "print" : pygame.K_PRINT,
                  "sysreq" : pygame.K_SYSREQ,
                  "break" : pygame.K_BREAK,
                  "menu" : pygame.K_MENU,
                  "power" : pygame.K_POWER,
                  "euro" : pygame.K_EURO,
                 }
