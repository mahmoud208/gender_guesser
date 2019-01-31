# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
import gender_guesser.detector as gender
d = gender.Detector()




a=[u'أحمد',u'إدريس',u'أدهم',u'أديب',u'أسعد',u'إسماعيل',u'أشرف',u'أصهب',u'أصيل',u'أكرم',u'أمجد',u'أمير',u'أنس',u'هناء']


for x in a :
    print(d.get_gender(x))




