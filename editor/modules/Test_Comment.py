#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""tests for Comment classes"""


import sys
import os.path
sys.path.append(os.path.join(sys.path[0], ".."))
import Comment
from PyQt4 import QtCore, QtGui
import unittest


class TestComment(unittest.TestCase):
    def setUp(self):
        self.commentObj = Comment.CommentDock(None)
        self.signalObj = testQObject()
        
    def testCheckModified(self):
        self.commentObj.ui.txtTranslatorComment.document().setModified(True)
        self.signalObj.connect(self.commentObj, QtCore.SIGNAL("commentChanged"), self.signalObj.slot)
        self.commentObj.checkModified()
        self.assertEqual(self.signalObj.slotReached, True)
        
class testQObject(QtCore.QObject):
    def __init__(self):
        self.slotReached = False
        
    def slot(self):
        self.slotReached = True
        print "hello"
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    unittest.main()
