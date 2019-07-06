#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def getreply():
    """
    Читает клавишу нажатую пользователем
    даже если stdin перенаправлен в файл или канал
    """
    # если stdin связан с консолью
    if sys.stdin.isatty():
        # читать ответ из stdin
        return input('?')
    # иначе - если stdin был перенаправлен
    # его нельзя использовать для чтения пользователя
    # обрабатываем в зависимости от платформы
    else:
        # Windows
        if sys.platform[:3] == 'win':
            import msvcrt                   # используем инструменты консоли windows
            msvcrt.putch(b'?')              # приглашение к вводу '?'
            key = msvcrt.getche()           # getche() - не выводит символ для нажатой
            msvcrt.putch(b'\n')             # клавиши
            return key
        # Linux
        elif sys.platform[:5] == 'linux':
            # в линуксе для чтения ввода с клавиатуры
            # достаточно подключиться к устройству /dev/tty
            print('?', end='', flush=True)
            tty = open('/dev/tty').readline()[:-1]
            return tty.encode()
        # Текущая платформа не поддерживается
        else:
            assert False, 'platform not supported'

if __name__ == '__main__':
    ent = getreply();
    print('ent=', ent)
