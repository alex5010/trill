#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import sys



con = None

try:



    #connect to Trill data base as a super user
    con = psycopg2.connect("dbname='trill' user='vagrant'")
    cur = con.cursor()




    cur.execute("DELETE FROM user_skills")
    cur.execute("DELETE FROM user_jobs")
    cur.execute("DELETE FROM skills")
    cur.execute("DELETE FROM skill_titles")
    cur.execute("DELETE FROM trill_role_skill_groups")
    cur.execute("DELETE FROM skill_groups")
    cur.execute("DELETE FROM job_titles")
    cur.execute("DELETE FROM trill_role_groups")
    cur.execute("DELETE FROM users")






    usercsv = open('/home/vagrant/trill/database-setup/load/usershashed.csv', 'r')
    cur.copy_from(usercsv, 'users', sep=',')

    trillrolegroupscsv = open('/home/vagrant/trill/database-setup/load/TrillRoleGroups.csv', 'r')
    cur.copy_from(trillrolegroupscsv, 'trill_role_groups', sep=',')


    jobtitlescsv = open('/home/vagrant/trill/database-setup/load/jobtitles.csv', 'r')
    cur.copy_from(jobtitlescsv, 'job_titles', sep=',')


    skillgroupscsv = open('/home/vagrant/trill/database-setup/load/SkillGroups.csv', 'r')
    cur.copy_from(skillgroupscsv, 'skill_groups', sep=',')


    skilltitlescsv = open('/home/vagrant/trill/database-setup/load/SkillTitles.csv', 'r')
    cur.copy_from(skilltitlescsv, 'skill_titles', sep=',')

    skillscsv = open('/home/vagrant/trill/database-setup/load/Skill.csv', 'r')
    cur.copy_from(skillscsv, 'skills', sep=',')

    userjobscsv = open('/home/vagrant/trill/database-setup/load/UserJobs.csv', 'r')
    cur.copy_from(userjobscsv, 'user_jobs', sep=',')

    userskillscsv = open('/home/vagrant/trill/database-setup/load/UserSkills.csv', 'r')
    cur.copy_from(userskillscsv, 'user_skills', sep=',')

    trillroleskillgroupscsv = open('/home/vagrant/trill/database-setup/load/TrillRoleSkillGroups.csv', 'r')
    cur.copy_from(trillroleskillgroupscsv, 'trill_role_skill_groups', sep=',')

    con.commit()


except psycopg2.DatabaseError as e:

    if con:
        con.rollback()

    print("Error: {0}".format(e))
    sys.exit(1)

finally:

    if con:
        con.close()
