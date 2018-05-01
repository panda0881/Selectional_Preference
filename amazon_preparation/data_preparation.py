import random
import json




def generate_object_question(tmp_verb, tmp_object, name, question_number):
    raw_data = """<fieldset><label>""" + str(
        question_number) + """. <font color="red"><b>('""" + tmp_verb + """', '""" + tmp_object + """')</b></font> : In your opinion, how suitable is <font color="red"><b>'""" + tmp_object + """'</b></font> as the <font color="blue"><b>object</b></font> of the verb <font color="red"><b>'""" + tmp_verb + """'</b></font>? </label>

<div class="object"><label><input name='""" + name + """' type="radio" value="5" />Perfectly match (<b>5</b>) </label></div>

<div class="object"><label><input name='""" + name + """' type="radio" value="4" />Make sense (<b>4</b>) </label></div>

<div class="object"><label><input name='""" + name + """' type="radio" value="3" />Normal (<b>3</b>) </label></div>

<div class="object"><label><input name='""" + name + """' type="radio" value="2" />Seems weird (<b>2</b>) </label></div>

<div class="object"><label><input name='""" + name + """' type="radio" value="1" />It's not applicable at all (<b>1</b>) </label></div>

<div class="object"><label><input name='""" + name + """' type="radio" value="-1" />I'm not sure </label></div>
</fieldset>"""
    return raw_data


def generate_subject_question(tmp_verb, tmp_subject, name, question_number):
    raw_data = """<fieldset><label>""" + str(
        question_number) + """. <font color="red"><b>('""" + tmp_subject + """', '""" + tmp_verb + """')</b></font> : In your opinion, how suitable is <font color="red"><b>'""" + tmp_subject + """'</b></font> as the <font color="blue"><b>subject</b></font> of the verb <font color="red"><b>'""" + tmp_verb + """'</b></font>? </label>

<div class="subject"><label><input name='""" + name + """' type="radio" value="5" />Perfectly match (<b>5</b>) </label></div>

<div class="subject"><label><input name='""" + name + """' type="radio" value="4" />Make sense (<b>4</b>) </label></div>

<div class="subject"><label><input name='""" + name + """' type="radio" value="3" />Normal (<b>3</b>) </label></div>

<div class="subject"><label><input name='""" + name + """' type="radio" value="2" />Seems weird (<b>2</b>) </label></div>

<div class="subject"><label><input name='""" + name + """' type="radio" value="1" />It's not applicable at all (<b>1</b>) </label></div>

<div class="subject"><label><input name='""" + name + """' type="radio" value="-1" />I'm not sure </label></div>
</fieldset>"""
    return raw_data


def generate_object_amod_question(tmp_verb, tmp_adj, name, question_number):
    raw_data = """<fieldset><label>""" + str(
        question_number) + """. <font color="red"><b>('""" + tmp_verb + """', '""" + tmp_adj + """')</b></font> : How suitable do you think if we use <font color="red"><b>'""" + tmp_adj + """'</b></font> to describe the <font color="blue"><b>object</b></font> of the verb <font color="red"><b>'""" + tmp_verb + """'</b></font>? </label>

<div class="object_amod"><label><input name='""" + name + """' type="radio" value="5" />Perfectly match (<b>5</b>) </label></div>

<div class="object_amod"><label><input name='""" + name + """' type="radio" value="4" />Make sense (<b>4</b>) </label></div>

<div class="object_amod"><label><input name='""" + name + """' type="radio" value="3" />Normal (<b>3</b>) </label></div>

<div class="object_amod"><label><input name='""" + name + """' type="radio" value="2" />Seems weird (<b>2</b>) </label></div>

<div class="object_amod"><label><input name='""" + name + """' type="radio" value="1" />It's not applicable at all (<b>1</b>) </label></div>

<div class="object_amod"><label><input name='""" + name + """' type="radio" value="-1" />I'm not sure </label></div>
</fieldset>"""
    return raw_data


def generate_subject_amod_question(tmp_verb, tmp_adj, name, question_number):
    raw_data = """<fieldset><label>""" + str(
        question_number) + """. <font color="red"><b>('""" + tmp_adj + """', '""" + tmp_verb + """')</b></font> : How suitable do you think if we use <font color="red"><b>'""" + tmp_adj + """'</b></font> to describe the <font color="blue"><b>subject</b></font> of the verb <font color="red"><b>'""" + tmp_verb + """'</b></font>? </label>

<div class="subject_amod"><label><input name='""" + name + """' type="radio" value="5" />Perfectly match (<b>5</b>) </label></div>

<div class="subject_amod"><label><input name='""" + name + """' type="radio" value="4" />Make sense (<b>4</b>) </label></div>

<div class="subject_amod"><label><input name='""" + name + """' type="radio" value="3" />Normal (<b>3</b>) </label></div>

<div class="subject_amod"><label><input name='""" + name + """' type="radio" value="2" />Seems weird (<b>2</b>) </label></div>

<div class="subject_amod"><label><input name='""" + name + """' type="radio" value="1" />It's not applicable at all (<b>1</b>) </label></div>

<div class="subject_amod"><label><input name='""" + name + """' type="radio" value="-1" />I'm not sure </label></div>
</fieldset>"""
    return raw_data


def generate_amod_question(tmp_noun, tmp_adj, name, question_number):
    raw_data = """<fieldset><label>""" + str(
        question_number) + """. <font color="red"><b>('""" + tmp_adj + """', '""" + tmp_noun + """')</b></font> : How suitable do you think if we use <font color="red"><b>'""" + tmp_adj + """'</b></font> to describe the noun <font color="red"><b>'""" + tmp_noun + """'</b></font>? </label>

<div class="amod"><label><input name='""" + name + """' type="radio" value="5" />Perfectly match (<b>5</b>) </label></div>

<div class="amod"><label><input name='""" + name + """' type="radio" value="4" />Make sense (<b>4</b>) </label></div>

<div class="amod"><label><input name='""" + name + """' type="radio" value="3" />Normal (<b>3</b>) </label></div>

<div class="amod"><label><input name='""" + name + """' type="radio" value="2" />Seems weird (<b>2</b>) </label></div>

<div class="amod"><label><input name='""" + name + """' type="radio" value="1" />It's not applicable at all (<b>1</b>) </label></div>

<div class="amod"><label><input name='""" + name + """' type="radio" value="-1" />I'm not sure </label></div>
</fieldset>"""
    return raw_data


def generate_check_English_question():
    raw_data = """<fieldset><label>* Please Answer this question to make sure that you are a native English speaker or you currently work/live in an English environment.  </label>

<div class="check_english"><label><input name='check_english' type="radio" value="1" />Yes (I am suitable for this job) </label></div>

<div class="check_english"><label><input name='check_english' type="radio" value="0" />No (I am <b>not</b> suitable for this job) </label></div>

</fieldset>"""
    return raw_data


def generate_object_questionnaire(verb_dict, verb_label_dict, selected_verbs, output_file_name):
    f = open(output_file_name, 'w')
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <section class="container" id="Other" style="margin-bottom:15px; padding: 10px 10px; font-family: Verdana, Geneva, sans-serif; color:#333333; font-size:0.9em;">
<div class="row col-xs-12 col-md-12"><!-- Instructions -->
<div class="panel panel-primary">
<div class="panel-heading"><strong>Instructions</strong></div>

<div class="panel-body">
<p>Relation between a verb and its object.</p>

<ul>
    <li>In this task, you will be asked to score a pair of a verb and its object based on how suitable you think this pair is. For example, <b>I love you</b>. In this example, <font color="red"><b>'you'</b></font> is the <font color="blue"><b>object</b></font> of the verb <font color="red"><b>'love'</b></font>.</li>
	<li>In some examples, a verb is always connected with a specific kind of objects. For example, <font color="red"><b>'eat'</b></font> and <font color="red"><b>'food'</b></font>. In this case, you should label this example with <b>5</b>.</li>
    <li>In some examples, a verb does not have certain preference with objects. For example, <font color="red"><b>'love'</b></font> and <font color="red"><b>'country'</b></font>. In this case, we can love anything, so you should label this example with <b>3</b>.</li>
    <li>In some examples, a verb is paired with a word that should not be its object. For example, <font color="red"><b>'eat'</b></font> and <font color="red"><b>'house'</b></font>. In this case, you should label this example with <b>1</b>.</li>
    <li>Anything between the above three situations, you can label them based on your feeling or commonsense. But if you don't know the meaning of these two words, please simply choose <b>'I'm not sure'</b>.</li>
    <li>You will be asked to label 103 questions. 3 very simple questions are randomly mixed into the dataset to make sure the quality of the annotation.</li>
    <li>PS: To finish this job, you must effectively label more than <b>80%</b> of the questions, which simply means that you can't choose <b>'I'm not sure'</b> for all the questions.</li>
</ul>
</div>
</div>
<!-- End Instructions --><!-- Content Body -->

<section>""")
    f.write('\n' + generate_check_English_question())
    tmp_verbs = selected_verbs + ['0', '1', '2']
    random.shuffle(tmp_verbs)
    tmp_question_number = 0
    for i, verb in enumerate(tmp_verbs):
        if verb == '0':
            tmp_question_number += 1
            name = 'dobj_check_0'
            tmp_question_html = generate_object_question(simple_checking_pairs['dobj'][0][0], simple_checking_pairs['dobj'][0][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        elif verb == '1':
            tmp_question_number += 1
            name = 'dobj_check_1'
            tmp_question_html = generate_object_question(simple_checking_pairs['dobj'][1][0], simple_checking_pairs['dobj'][1][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        elif verb == '2':
            tmp_question_number += 1
            name = 'dobj_check_2'
            tmp_question_html = generate_object_question(simple_checking_pairs['dobj'][2][0], simple_checking_pairs['dobj'][2][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        else:
            tmp_objects = verb_dict[verb] + []
            random.shuffle(tmp_objects)
            for tmp_object in tmp_objects:
                tmp_question_number += 1
                verb_pos = verb_label_dict[verb]
                name = 'dobj_v' + str(verb_pos) + '_' + str(verb_dict[verb].index(tmp_object) + 1)
                tmp_question_html = generate_object_question(verb, tmp_object, name, tmp_question_number)
                f.write('\n')
                f.write(tmp_question_html)
    f.write("""</section>
<!-- End Content Body --></div>
</section>
<style type="text/css">fieldset { padding: 10px; background:#fbfbfb; border-radius:5px; margin-bottom:5px; }
</style>

</head>
<body>

</body>
</html>""")
    f.close()


def generate_subject_questionnaire(verb_dict, verb_label_dict, selected_verbs, output_file_name):
    f = open(output_file_name, 'w')
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <section class="container" id="Other" style="margin-bottom:15px; padding: 10px 10px; font-family: Verdana, Geneva, sans-serif; color:#333333; font-size:0.9em;">
<div class="row col-xs-12 col-md-12"><!-- Instructions -->
<div class="panel panel-primary">
<div class="panel-heading"><strong>Instructions</strong></div>

<div class="panel-body">
<p>Relation between a verb and its subject.</p>

<ul>
    <li>In this task, you will be asked to score a pair of a verb and its subject based on how suitable you think this pair is. For example, <b>I love you</b>. In this example, <font color="red"><b>'I'</b></font> is the <font color="blue"><b>subject</b></font> of the verb <font color="red"><b>'love'</b></font>.</li>
	<li>In some examples, a verb is always connected with a specific kind of subjects. For example, <font color="red"><b>'dog'</b></font> and <font color="red"><b>'bark'</b></font>. In this case, you should label this example with <b>5</b>.</li>
    <li>In some examples, a verb does not have certain preference with objects. For example, <font color="red"><b>'people'</b></font> and <font color="red"><b>'live'</b></font>. In this case, Everything can live, so you should label this example with <b>3</b>.</li>
    <li>In some examples, a verb is paired with a word that should not be its object. For example, <font color="red"><b>'house'</b></font> and <font color="red"><b>'eat'</b></font>. In this case, you should label this example with <b>1</b>.</li>
    <li>Anything between the above three situations, you can label them based on your feeling or commonsense. But if you don't know the meaning of these two words, please simply choose <b>'I'm not sure'</b>.</li>
    <li>You will be asked to label 103 questions. 3 very simple questions are randomly mixed into the dataset to make sure the quality of the annotation.</li>
    <li>PS: To finish this job, you must effectively label more than <b>80%</b> of the questions, which simply means that you can't choose <b>'I'm not sure'</b> for all the questions.</li>
</ul>
</div>
</div>
<!-- End Instructions --><!-- Content Body -->

<section>""")
    f.write('\n' + generate_check_English_question())
    tmp_verbs = selected_verbs + ['0', '1', '2']
    random.shuffle(tmp_verbs)
    tmp_question_number = 0
    for i, verb in enumerate(tmp_verbs):
        if verb == '0':
            tmp_question_number += 1
            name = 'subj_check_0'
            tmp_question_html = generate_subject_question(simple_checking_pairs['nsubj'][0][0], simple_checking_pairs['nsubj'][0][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        elif verb == '1':
            tmp_question_number += 1
            name = 'subj_check_1'
            tmp_question_html = generate_subject_question(simple_checking_pairs['nsubj'][1][0], simple_checking_pairs['nsubj'][1][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        elif verb == '2':
            tmp_question_number += 1
            name = 'subj_check_2'
            tmp_question_html = generate_subject_question(simple_checking_pairs['nsubj'][2][0], simple_checking_pairs['nsubj'][2][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        else:
            tmp_nsubjs = verb_dict[verb] + []
            random.shuffle(tmp_nsubjs)
            for tmp_nsubj in tmp_nsubjs:
                tmp_question_number += 1
                verb_pos = verb_label_dict[verb]
                name = 'subj_v' + str(verb_pos) + '_' + str(verb_dict[verb].index(tmp_nsubj) + 1)
                tmp_question_html = generate_subject_question(verb, tmp_nsubj, name, tmp_question_number)
                f.write('\n')
                f.write(tmp_question_html)
    f.write("""</section>
<!-- End Content Body --></div>
</section>
<style type="text/css">fieldset { padding: 10px; background:#fbfbfb; border-radius:5px; margin-bottom:5px; }
</style>

</head>
<body>

</body>
</html>""")
    f.close()


def generate_object_amod_questionnaire(verb_dict, verb_label_dict, selected_verbs, output_file_name):
    f = open(output_file_name, 'w')
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <section class="container" id="Other" style="margin-bottom:15px; padding: 10px 10px; font-family: Verdana, Geneva, sans-serif; color:#333333; font-size:0.9em;">
<div class="row col-xs-12 col-md-12"><!-- Instructions -->
<div class="panel panel-primary">
<div class="panel-heading"><strong>Instructions</strong></div>

<div class="panel-body">
<p>Relation between a verb and the adjective of its object.</p>

<ul>
    <li>In this task, you will be asked to score a pair of a verb and the adjective of its object based on how suitable you think this pair is. For example, <b>I love this beautiful country</b>. In this example, <font color="blue"><b>'country'</b></font> is the <font color="blue"><b>object</b></font> of the verb <font color="red"><b>'love'</b></font> and <font color="red"><b>'beautiful'</b></font> is the adjective we use to describe its <font color="blue"><b>object</b></font>.</li>
	<li>In some examples, we always use a specific kind of adjectives to describe the object of a verb. For example, <font color="red"><b>'eat'</b></font> and <font color="red"><b>'tasty'</b></font> food. In this case, you should label this example with <b>5</b>.</li>
    <li>In some examples, we can use any adjectives to describe the object of a verb. For example, <font color="red"><b>'buy'</b></font> and <font color="red"><b>'fancy'</b></font> car. In this case, we can use any adjectives to describe the staff we bought, so you should label this example with <b>3</b>.</li>
    <li>In some examples, a adjective is not supposed to be used to describe the object of a verb. For example, <font color="red"><b>'read'</b></font> and <font color="red"><b>'tasty'</b></font> book. In this case, you should label this example with <b>1</b>.</li>
    <li>Anything between the above three situations, you can label them based on your feeling or commonsense. But if you don't know the meaning of these two words, please simply choose <b>'I'm not sure'</b>.</li>
    <li>You will be asked to label 103 questions. 3 very simple questions are randomly mixed into the dataset to make sure the quality of the annotation.</li>
    <li>PS: To finish this job, you must effectively label more than <b>80%</b> of the questions, which simply means that you can't choose <b>'I'm not sure'</b> for all the questions.</li>
</ul>
</div>
</div>
<!-- End Instructions --><!-- Content Body -->

<section>""")
    f.write('\n' + generate_check_English_question())
    tmp_verbs = selected_verbs + ['0', '1', '2']
    random.shuffle(tmp_verbs)
    tmp_question_number = 0
    for i, verb in enumerate(tmp_verbs):
        if verb == '0':
            tmp_question_number += 1
            name = 'dobj_amod_check_0'
            tmp_question_html = generate_object_amod_question(simple_checking_pairs['dobj_amod'][0][0], simple_checking_pairs['dobj_amod'][0][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        elif verb == '1':
            tmp_question_number += 1
            name = 'dobj_amod_check_1'
            tmp_question_html = generate_object_amod_question(simple_checking_pairs['dobj_amod'][1][0], simple_checking_pairs['dobj_amod'][1][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        elif verb == '2':
            tmp_question_number += 1
            name = 'dobj_amod_check_2'
            tmp_question_html = generate_object_amod_question(simple_checking_pairs['dobj_amod'][2][0], simple_checking_pairs['dobj_amod'][2][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        else:
            tmp_object_amods = verb_dict[verb] + []
            random.shuffle(tmp_object_amods)
            for tmp_object_amod in tmp_object_amods:
                tmp_question_number += 1
                verb_pos = verb_label_dict[verb]
                name = 'dobj_amod_v' + str(verb_pos) + '_' + str(verb_dict[verb].index(tmp_object_amod) + 1)
                tmp_question_html = generate_object_amod_question(verb, tmp_object_amod, name, tmp_question_number)
                f.write('\n')
                f.write(tmp_question_html)
    f.write("""</section>
<!-- End Content Body --></div>
</section>
<style type="text/css">fieldset { padding: 10px; background:#fbfbfb; border-radius:5px; margin-bottom:5px; }
</style>

</head>
<body>

</body>
</html>""")
    f.close()


def generate_subj_amod_questionnaire(verb_dict, verb_label_dict, selected_verbs, output_file_name):
    f = open(output_file_name, 'w')
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <section class="container" id="Other" style="margin-bottom:15px; padding: 10px 10px; font-family: Verdana, Geneva, sans-serif; color:#333333; font-size:0.9em;">
<div class="row col-xs-12 col-md-12"><!-- Instructions -->
<div class="panel panel-primary">
<div class="panel-heading"><strong>Instructions</strong></div>

<div class="panel-body">
<p>Relation between a verb and the adjective of its subject.</p>

<ul>
    <li>In this task, you will be asked to score a pair of a verb and the adjective of its subject based on how suitable you think this pair is. For example, <b>The hungry boy eats the burger.</b>. In this example, <font color="blue"><b>'boy'</b></font> is the <font color="blue"><b>subject</b></font> of the verb <font color="red"><b>'eat'</b></font> and <font color="red"><b>'hungry'</b></font> is the adjective we use to describe its <font color="blue"><b>'subject'</b></font>.</li>
	<li>In some examples, we always use a specific kind of adjectives to describe the subject of a verb. For example, <font color="red"><b>'hungry'</b></font> boy and <font color="red"><b>'eat'</b></font>. In this case, you should label this example with <b>5</b>.</li>
    <li>In some examples, we can use any adjectives to describe the subject of a verb. For example, <font color="red"><b>'handsome'</b></font> boy and <font color="red"><b>'study'</b></font> car. In this case, we can use any adjectives to describe the person who study, so you should label this example with <b>3</b>.</li>
    <li>In some examples, an adjective is not supposed to be used to describe the subject of a verb. For example, <font color="red"><b>'tasty'</b></font> boy and <font color="red"><b>'study'</b></font>. In this case, you should label this example with <b>1</b>.</li>
    <li>Anything between the above three situations, you can label them based on your feeling or commonsense. But if you don't know the meaning of these two words, please simply choose <b>'I'm not sure'</b>.</li>
    <li>You will be asked to label 103 questions. 3 very simple questions are randomly mixed into the dataset to make sure the quality of the annotation.</li>
    <li>PS: To finish this job, you must effectively label more than <b>80%</b> of the questions, which simply means that you can't choose <b>'I'm not sure'</b> for all the questions.</li>
</ul>
</div>
</div>
<!-- End Instructions --><!-- Content Body -->

<section>""")
    f.write('\n' + generate_check_English_question())
    tmp_verbs = selected_verbs + ['0', '1', '2']
    random.shuffle(tmp_verbs)
    tmp_question_number = 0
    for i, verb in enumerate(tmp_verbs):
        if verb == '0':
            tmp_question_number += 1
            name = 'nsubj_amod_check_0'
            tmp_question_html = generate_subject_amod_question(simple_checking_pairs['nsubj_amod'][0][0], simple_checking_pairs['nsubj_amod'][0][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        elif verb == '1':
            tmp_question_number += 1
            name = 'nsubj_amod_check_1'
            tmp_question_html = generate_subject_amod_question(simple_checking_pairs['nsubj_amod'][1][0], simple_checking_pairs['nsubj_amod'][1][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        elif verb == '2':
            tmp_question_number += 1
            name = 'nsubj_amod_check_2'
            tmp_question_html = generate_subject_amod_question(simple_checking_pairs['nsubj_amod'][2][0], simple_checking_pairs['nsubj_amod'][2][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        else:
            tmp_nsubject_amods = verb_dict[verb] + []
            random.shuffle(tmp_nsubject_amods)
            for tmp_nsubject_amod in tmp_nsubject_amods:
                tmp_question_number += 1
                verb_pos = verb_label_dict[verb]
                name = 'nsubj_amod_v' + str(verb_pos) + '_' + str(verb_dict[verb].index(tmp_nsubject_amod) + 1)
                tmp_question_html = generate_subject_amod_question(verb, tmp_nsubject_amod, name, tmp_question_number)
                f.write('\n')
                f.write(tmp_question_html)
    f.write("""</section>
<!-- End Content Body --></div>
</section>
<style type="text/css">fieldset { padding: 10px; background:#fbfbfb; border-radius:5px; margin-bottom:5px; }
</style>

</head>
<body>

</body>
</html>""")
    f.close()


def generate_amod_questionnaire(noun_dict, noun_label_dict, selected_nouns, output_file_name):
    f = open(output_file_name, 'w')
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <section class="container" id="Other" style="margin-bottom:15px; padding: 10px 10px; font-family: Verdana, Geneva, sans-serif; color:#333333; font-size:0.9em;">
<div class="row col-xs-12 col-md-12"><!-- Instructions -->
<div class="panel panel-primary">
<div class="panel-heading"><strong>Instructions</strong></div>

<div class="panel-body">
<p>Relation between a noun and its adjective.</p>

<ul>
    <li>In this task, you will be asked to score a pair of a noun and its adjective based on how suitable you think this pair is. For example, <b>Beautiful Flower</b>. In this example, <font color="red"><b>'beautiful'</b></font> is the <font color="blue"><b>adjective</b></font> of the noun <font color="red"><b>'flower'</b></font>.</li>
	<li>In some examples, an adjective is always used to describe a specific kind of nouns. For example, <font color="red"><b>'tasty'</b></font> and <font color="red"><b>'food'</b></font>. In this case, you should label this example with <b>5</b>.</li>
    <li>In some examples, an adjective can be used to describe any nouns. For example, <font color="red"><b>'large'</b></font> and <font color="red"><b>'house'</b></font>. In this case, we can use large to describe almost everything, so you should label this example with <b>3</b>.</li>
    <li>In some examples, an adjective is not supposed to be used to describe a noun. For example, <font color="red"><b>'tasty'</b></font> and <font color="red"><b>'rock'</b></font>. In this case, you should label this example with <b>1</b>.</li>
    <li>Anything between the above three situations, you can label them based on your feeling or commonsense. But if you don't know the meaning of these two words, please simply choose <b>'I'm not sure'</b>.</li>
    <li>You will be asked to label 103 questions. 3 very simple questions are randomly mixed into the dataset to make sure the quality of the annotation.</li>
    <li>PS: To finish this job, you must effectively label more than <b>80%</b> of the questions, which simply means that you can't choose <b>'I'm not sure'</b> for all the questions.</li>
</ul>
</div>
</div>
<!-- End Instructions --><!-- Content Body -->

<section>""")
    f.write('\n' + generate_check_English_question())
    tmp_nouns = selected_nouns + ['0', '1', '2']
    random.shuffle(tmp_nouns)
    tmp_question_number = 0
    for i, noun in enumerate(tmp_nouns):
        if noun == '0':
            tmp_question_number += 1
            name = 'amod_check_0'
            tmp_question_html = generate_amod_question(simple_checking_pairs['amod'][0][0], simple_checking_pairs['amod'][0][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        elif noun == '1':
            tmp_question_number += 1
            name = 'amod_check_1'
            tmp_question_html = generate_amod_question(simple_checking_pairs['amod'][1][0], simple_checking_pairs['amod'][1][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        elif noun == '2':
            tmp_question_number += 1
            name = 'amod_check_2'
            tmp_question_html = generate_amod_question(simple_checking_pairs['amod'][2][0], simple_checking_pairs['amod'][2][1], name, tmp_question_number)
            f.write('\n')
            f.write(tmp_question_html)
        else:
            tmp_adjs = noun_dict[noun] + []
            random.shuffle(tmp_adjs)
            for tmp_adj in tmp_adjs:
                tmp_question_number += 1
                verb_pos = noun_label_dict[noun]
                name = 'amod_n' + str(verb_pos) + '_' + str(noun_dict[noun].index(tmp_adj) + 1)
                tmp_question_html = generate_amod_question(noun, tmp_adj, name, tmp_question_number)
                f.write('\n')
                f.write(tmp_question_html)
    f.write("""</section>
<!-- End Content Body --></div>
</section>
<style type="text/css">fieldset { padding: 10px; background:#fbfbfb; border-radius:5px; margin-bottom:5px; }
</style>

</head>
<body>

</body>
</html>""")
    f.close()

simple_checking_pairs = dict()
simple_checking_pairs['dobj'] = [('eat', 'food'), ('love', 'country'), ('eat', 'house')]
simple_checking_pairs['dobj_amod'] = [('eat', 'tasty'), ('buy', 'fancy'), ('read', 'tasty')]
simple_checking_pairs['nsubj'] = [('bark', 'dog'), ('live', 'people'), ('eat', 'house')]
simple_checking_pairs['nsubj_amod'] = [('eat', 'hungry'), ('study', 'handsome'), ('study', 'tasty')]
simple_checking_pairs['amod'] = [('food', 'tasty'), ('house', 'large'), ('rock', 'tasty')]

# relation_dict = dict()
# for verb in sample_verbs:
#     relation_dict[verb] = dict()
#     relation_dict[verb]['dobj'] = ['noun1', 'noun2', 'noun3', 'noun4', 'noun5']
#     relation_dict[verb]['dobj_amod'] = ['adj1', 'adj2', 'adj3', 'adj4', 'adj5']
#     relation_dict[verb]['nsubj'] = ['noun1', 'noun2', 'noun3', 'noun4', 'noun5']
#     relation_dict[verb]['nsubj_amod'] = ['adj1', 'adj2', 'adj3', 'adj4', 'adj5']

# with open('../test_100.json', 'r') as f:
#     relation_dict = json.load(f)
#
# with open('../verb_dict.json', 'r') as f:
#     verb_pos_dict = json.load(f)


# tmp_pairs = list()
# for tmp_verb in sample_verbs:
#     related_words = relation_dict[tmp_verb]['dobj']
#     for w in related_words:
#         tmp_pairs.append((tmp_verb, w))

# verb_pos_dict = dict()
# for i, verb in enumerate(sample_verbs):
#     verb_pos_dict[verb] = str(i + 1)

# sample_verbs = list()
# for tmp_verb in relation_dict:
#     sample_verbs.append(tmp_verb)

# generate_object_questionnaire(relation_dict, verb_pos_dict, sample_verbs, 'test_object.html')
# generate_subject_questionnaire(relation_dict, verb_pos_dict, sample_verbs, 'test_subject.html')
# generate_object_amod_questionnaire(relation_dict, verb_pos_dict, sample_verbs, 'test_object_amod.html')
# generate_subj_amod_questionnaire(relation_dict, verb_pos_dict, sample_verbs, 'test_subject_amod.html')

nsubj_amod_dict = dict()
all_verbs = list()
verb_pos_dict = dict()
with open('../nsubj_amod_pairs.txt', 'r') as f:
    counter = 0
    for line in f:
        counter += 1
        words = line[:-1].split('\t')
        nsubj_amod_dict[words[0]] = [words[1], words[2], words[3], words[4]]
        all_verbs.append(words[0])
        verb_pos_dict[words[0]] = counter

for i in range(20):
    selected_verbs = all_verbs[i*25: (i+1)*25]
    file_name = 'nsubj_amod/nsubj_amod_' + str(i+1) + '.html'
    generate_subj_amod_questionnaire(nsubj_amod_dict, verb_pos_dict, selected_verbs, file_name)

print('end')
