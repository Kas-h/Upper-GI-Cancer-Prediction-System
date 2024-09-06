from django.shortcuts import render
from joblib import load

model = load('./savedModels/model.joblib')

histology_mapping = {"ACC": 0, "SCC": 2}
sex_mapping = {"F": 0, "M": 1}
ml_mapping = {"Decision_Tree_Classifier": 0, "Random_Forest_Classifier": 1,"Support_Vector_Machine":2}

def predictor(request):
    if request.method == 'POST':


        ml_str = request.POST['ML_Model']
        histology_str = request.POST['Histology']
        sex_str = request.POST['Sex']

        ML_Model = ml_mapping.get(ml_str,-1)
        Sex = sex_mapping.get(sex_str, -1)
        Age = request.POST['Age']
        Weight = request.POST['Weight']
        Height = request.POST['Height']
        Histology = histology_mapping.get(histology_str, -1)

        Pre_op_CRP_level = request.POST['Pre_op_CRP_level']
        Pre_op_Bili = request.POST['Pre_op_Bili']
        Pre_op_ALT = request.POST['Pre_op_ALT']
        Pre_op_Alk_Phos = request.POST['Pre_op_Alk_Phos']
        Pre_op_GGT = request.POST['Pre_op_GGT']
        Pre_op_Albumin = request.POST['Pre_op_Albumin']
        Pre_op_Urea = request.POST['Pre_op_Urea']
        Pre_op_Creatinine = request.POST['Pre_op_Creatinine']
        Pre_op_estimated_GFR = request.POST['Pre_op_estimated_GFR']
        Pre_op_Na = request.POST['Pre_op_Na']
        Pre_op_K = request.POST['Pre_op_K']
        Pre_op_TCO2 = request.POST['Pre_op_TCO2']
        Pre_op_Glucose = request.POST['Pre_op_Glucose']
        Pre_op_Hb = request.POST['Pre_op_Hb']
        Pre_op_PLT = request.POST['Pre_op_PLT']
        Pre_op_WCC = request.POST['Pre_op_WCC']
        Blood_testosterone = request.POST['Blood_testosterone']
        Blood_calc_free_testosterone = request.POST['Blood_calc_free_testosterone']
        Blood_oestradiol = request.POST['Blood_oestradiol']
        Blood_LH = request.POST['Blood_LH']
        Blood_FSH = request.POST['Blood_FSH']
        Blood_SHBG = request.POST['Blood_SHBG']
        Blood_insulin = request.POST['Blood_insulin']
        Blood_cortisol = request.POST['Blood_cortisol']

        Test = model.predict([[Age, Sex, Weight, Height, Histology, Pre_op_CRP_level, Pre_op_Bili, Pre_op_ALT, Pre_op_Alk_Phos, Pre_op_GGT, Pre_op_Albumin, Pre_op_Urea, Pre_op_Creatinine, Pre_op_estimated_GFR, Pre_op_Na, Pre_op_K, Pre_op_TCO2, Pre_op_Glucose, Pre_op_Hb, Pre_op_PLT, Pre_op_WCC, Blood_testosterone, Blood_calc_free_testosterone, Blood_oestradiol, Blood_LH, Blood_FSH, Blood_SHBG, Blood_insulin, Blood_cortisol]])
        Test2 = model.predict([[Age, Sex, Weight, Height, Histology, Pre_op_CRP_level, Pre_op_Bili, Pre_op_ALT, Pre_op_Alk_Phos, Pre_op_GGT, Pre_op_Albumin, Pre_op_Urea, Pre_op_Creatinine, Pre_op_estimated_GFR, Pre_op_Na, Pre_op_K, Pre_op_TCO2, Pre_op_Glucose, Pre_op_Hb, Pre_op_PLT, Pre_op_WCC, Blood_testosterone, Blood_calc_free_testosterone, Blood_oestradiol, Blood_LH, Blood_FSH, Blood_SHBG, Blood_insulin, Blood_cortisol]])
        Test3 = model.predict([[Age, Sex, Weight, Height, Histology, Pre_op_CRP_level, Pre_op_Bili, Pre_op_ALT, Pre_op_Alk_Phos, Pre_op_GGT, Pre_op_Albumin, Pre_op_Urea, Pre_op_Creatinine, Pre_op_estimated_GFR, Pre_op_Na, Pre_op_K, Pre_op_TCO2, Pre_op_Glucose, Pre_op_Hb, Pre_op_PLT, Pre_op_WCC, Blood_testosterone, Blood_calc_free_testosterone, Blood_oestradiol, Blood_LH, Blood_FSH, Blood_SHBG, Blood_insulin, Blood_cortisol]])
        

        if ML_Model==0:
            if Test[0]==0:
                Test = 'Gastric'
            elif Test[0]==1:
                Test = 'OGJ'
            elif Test[0]==2:
                Test = 'Oesophagus'
            elif Test[0]==3:
                Test = 'Pancreas'
        
        elif ML_Model==1:
            if Test2[0]==0:
                Test2 = 'Gastric'
            elif Test2[0]==1:
                Test2 = 'OGJ'
            elif Test2[0]==2:
                Test2 = 'Oesophagus'
            elif Test2[0]==3:
                Test2 = 'Pancreas'

        elif ML_Model==2:
            if Test3[0]==0:
                Test3 = 'Gastric'
            elif Test3[0]==1:
                Test3 = 'OGJ'
            elif Test3[0]==2:
                Test3 = 'Oesophagus'
            elif Test3[0]==3:
                Test3 = 'Pancreas'
        if Test[0]==0:
            Test = 'Gastric'
        elif Test[0]==1:
            Test = 'OGJ'
        elif Test[0]==2:
            Test = 'Oesophagus'
        elif Test[0]==3:
            Test = 'Pancreas'
            
        return render(request,'main.html',{'result' : Test})
    return render(request,'main.html')
