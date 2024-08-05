# 2235. 两整数相加
# https://leetcode.cn/problems/add-two-integers/

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

# from ctypes import *
# import mmap
#
#
# def translate(asm_code):
#     res = b''
#     for line in asm_code.split('\n'):
#         if ':' not in line or '>:' in line:
#             continue
#         line = line[line.find(':') + 1:].strip()
#         line = line[:line.find('   ')].strip()
#         for b in line.split(' '):
#             res += int(b, 16).to_bytes(1, byteorder='little')
#     return res
#
#
# buf = mmap.mmap(-1, mmap.PAGESIZE, prot=mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC)
#
#
# def compile_asm(asm_code, ftype):
#     buf.write(translate(asm_code))
#     return ftype(addressof(c_void_p.from_buffer(buf)))
#
#
# fn = compile_asm(
#     """
#     0:  55                      push   rbp
#     1:  48 89 e5                mov    rbp,rsp
#     4:  89 7d fc                mov    DWORD PTR [rbp-0x4],edi
#     7:  89 75 f8                mov    DWORD PTR [rbp-0x8],esi
#     a:  8b 55 fc                mov    edx,DWORD PTR [rbp-0x4]
#     d:  8b 45 f8                mov    eax,DWORD PTR [rbp-0x8]
#     10: 01 d0                   add    eax,edx
#     12: 5d                      pop    rbp
#     13: c3                      ret
#     """,
#     CFUNCTYPE(c_int, c_int, c_int)
# )
#
#
# class Solution:
#     def sum(self, a: int, b: int) -> int:
#         return fn(a, b)