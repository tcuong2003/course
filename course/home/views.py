import os, re
import pandas as pd
from django.shortcuts import render

def get_home(request):
    file_path = '/Users/trancuong/Library/Mobile Documents/com~apple~CloudDocs/FPT_Course/course/home/data_csv/Java Web Developer_data.csv'

   
    data = pd.read_csv(file_path)

    
    course_name = data['course'].iloc[0]
    sub_course_list = data['sub_course'].dropna().unique()

    sub_courses_data = {}
    
    for index, row in data.iterrows():
        sub_course = row['sub_course']
        module_name = row['module']
        sub_module_name = row['sub_module']
        
        if sub_course not in sub_courses_data:
            sub_courses_data[sub_course] = {}

        
        if module_name not in sub_courses_data[sub_course]:
            sub_courses_data[sub_course][module_name] = []
        
        if pd.notna(sub_module_name):
            sub_courses_data[sub_course][module_name].append({
                'sub_module': sub_module_name,
                'content_html_list': row['content_html_list'] if pd.notna(row['content_html_list']) else '',
                'img_list': row['img_list'] if pd.notna(row['img_list']) else '',
                'video_url': row['video_url'] if pd.notna(row['video_url']) else ''
            })

    
    split_sub_courses = []
    for sub_course in sub_course_list:
        if ':' in sub_course:
            title, description = sub_course.split(':', 1)
            split_sub_courses.append({
                'title': title.strip(),
                'description': description.strip(),
                'modules': sub_courses_data[sub_course] 
            })

   
    context = {
        'course_name': course_name,
        'split_sub_courses': split_sub_courses,  
    }

    
    return render(request, 'home.html', context)
