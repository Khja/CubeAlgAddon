from .cube import *
from anki.hooks import addHook
from aqt import mw
from anki.consts import *
import os
from aqt.qt import *


# MIT License
# Copyright (c) 2020 Khja
# Please read before using this piece of software.


VERSION = '2.0'
FIELDS = ['Case',
          'Notes',
          'Algorithm',
          'U Algorithm',
          "U' Algorithm",
          "U2 Algorithm",
          "Scramble",
          "ScrambleSize",
          "Neutrality",
          "U",
          "U'",
          "U2"]
MODEL_NAME = 'Cube Algorithm'+' ('+VERSION+')'
MODEL_TYPE = 'cubalg'



# Setup
def addModel1(col):
    """Add add-on note type to collection"""
    models = col.models
    model = models.new(MODEL_NAME)
    
    #Add fields
    for i in FIELDS:
        fld = models.newField(i)
        models.addField(model,fld)
        
    # Add template
    ##How to add two different front sides?
    m_n = models.newTemplate("Position: Normal")
    models.addTemplate(model, m_n)

    m_u = models.newTemplate("Position: U")
    models.addTemplate(model, m_u)

    m_ui = models.newTemplate("Position: U'")
    models.addTemplate(model, m_ui)

    m_u2 = models.newTemplate("Position: U2")
    models.addTemplate(model, m_u2)

    model['tmpls'][0]['qfmt'] = n_front
    model['tmpls'][0]['afmt'] = n_back
    model['tmpls'][1]['qfmt'] = u_front
    model['tmpls'][1]['afmt'] = u_back
    model['tmpls'][2]['qfmt'] = ui_front
    model['tmpls'][2]['afmt'] = ui_back
    model['tmpls'][3]['qfmt'] = u2_front
    model['tmpls'][3]['afmt'] = u2_back

    model['css'] = css
    models.add(model)
    models.save(model)
    return model


def setupAddon():
    #Check if there's already a card type called MODEL_NAME
    model = mw.col.models.byName(MODEL_NAME)
    
    if not model:
        model = addModel1(mw.col)

addHook("profileLoaded", setupAddon)
