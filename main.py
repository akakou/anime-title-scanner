#!/usr/bin/env python
'''example/scanner.py
This is the sample code of scanner.
'''

from pykakasi import kakasi,wakati
from filt.scanner import BaseScanner 
import sys

# **DO NOT use** stdin and stdout.
# Scanner use them to communicate with filt.

class SampleScanner(BaseScanner):
    '''
    This is the sample scanner.
    '''

    def ready(self, target):
        self.target = target.decode('utf-8')

        _kakasi = kakasi()
        _kakasi.setMode("r","Hepburn")
        _kakasi.setMode("H","K")
        _kakasi.setMode("J","K")
        conv = _kakasi.getConverter()

        self.katakana = conv.do(self.target)

    def scan(self, target, signature):
        '''
        Check target and signature are same.
        '''

        signatures = signature.decode('utf-8').split('\n')

        for signature in signatures:
            signature = signature.split(',')

            if len(signature) <= 6:
                continue

            if signature[4] and (signature[4] in target) and (len(signature[4]) > 2):
                sys.stderr.write(f"{signature[4]}:{target} \n\n")
                return (True, signature[4])

            if signature[6] and (signature[6] in self.katakana and (len(signature[6]) > 3)):
                sys.stderr.write(f"{signature[6]}:{target} \n\n")
                return (True, signature[4])
        
        return (False, "")


if __name__ == '__main__':
    # run scanner
    sample_scanner = SampleScanner()
    sample_scanner.run()
