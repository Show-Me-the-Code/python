# --*-- encoding:utf-8 --*--
#�� 0001 �⣺ ��Ϊ Apple Store App ���������ߣ���Ҫ����ʱ������Ϊ���Ӧ�����ɼ���
#�루�����Ż�ȯ����ʹ�� Python ������� 200 �������루�����Ż�ȯ����
from __future__ import print_function
import random,sys
def activecode(cc,cl):
    codechart='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for cc in range(0,cc):
        s=[random.choice(codechart) for i in range(cl)]
        print(''.join(s))

if __name__ =='__main__':
    activecode(20,32)
