import operator
from tkinter import *
import tkinter
import customtkinter

class Environment():
    myGraph = {"Gate_A": set(["Procurement", "Administration_Block", "Administration_Parking"]),
               "Administration_Block": set(
                   ["Lillian_K_Beam", "Gate_A", "Administration_Parking", "Mama_Africa", "Transport_Office",
                    "Lillian_K_Beam_Parking"]),
               "Lillian_K_Beam_Parking": set(
                   ["Lillian_K_Beam", "Administration_Parking", "Administration_Block", "Cafeteria"]),
               "Administration_Parking": set(
                   ["Gate_A", "Transport_Office", "Administration_Block", "Lillian_K_Beam_Parking"]),
               "Main_Lab": set(
                   ["Old_Humanities", "Mama_Africa", "Lillian_K_Beam", "Cafeteria", "Wooden_Blocks", "Hostels",
                    "Basketball_Court", "Library", "Procurement", "Auditorium", "School_of_Business"]),
               "Procurement": set(["Wooden_Blocks", "Mama_Africa", "Gate_A", "Main_Lab"]),
               "Mama_Africa": set(
                   ["Lillian_K_Beam", "Wooden_Blocks", "Procurement", "Administration_Block", "Main_Lab"]),
               "Wooden_Blocks": set(["Main_Lab", "Procurement", "Cafeteria", "Mama_Africa", "Old_Humanities"]),
               "Lillian_K_Beam": set(
                   ["Cafeteria", "Administration_Block", "Main_Lab", "Mama_Africa", "Lillian_K_Beam_Parking"]),
               "Cafeteria": set(
                   ["Lillian_K_Beam", "Wooden_Blocks", "Main_Lab", "Hostels",
                    "Library", "Auditorium", "School_of_Business", "Old_Humanities", "Transport_Office",
                    "Basketball_Court", "Lillian_K_Beam_Parking"]),

               "Old_Humanities": set(
                   ["Wooden_Blocks", "School_of_Business", "Main_Lab", "Auditorium", "Library", "Cafeteria",
                    "Hostels", "Basketball_Court"]),
               "School_of_Business": set(
                   ["Old_Humanities", "Main_Lab", "Auditorium", "Library", "Cafeteria", "Hostels",
                    "Basketball_Court"]),
               "Hostels": set(
                   ["Cafeteria", "Cafe_Latta", "School_of_Business", "Auditorium", "Library", "Old_Humanities",
                    "Main_Lab", "Transport_Office", "Basketball_Court"]),
               "Cyber_Cafe": set(["Cafe_Latta", "Auditorium", "Library", "Basketball_Court", "Bus_Parking_Lot"]),
               "Transport_Office": set(
                   ["Cafe_Latta", "Hostels", "Administration_Parking", "Cafeteria", "Administration_Block",
                    "Cafe_Latta_Parking_Lot"]),
               "Cafe_Latta": set(["Cafe_Latta_Parking_Lot", "Hostels", "Transport_Office", "Bus_Parking_Lot",
                                  "Cyber_Cafe"]),
               "Cafe_Latta_Parking_Lot": set(
                   ["Bus_Parking_Lot", "Cafe_Latta", "Faculty_Housing", "Student_Centre_Parking", "Hostels",
                    "Transport_Office"]),
               "Basketball_Court": set(["Cyber_Cafe", "Bus_Parking_Lot", "Auditorium", "Library",
                                        "School_of_Business", "Old_Humanities", "Cafeteria",
                                        "Student_Centre_Parking", "Student_Centre", "Main_Lab", "Hostels"]),
               "Auditorium": set(["Basketball_Court", "Library", "Auditorium_Parking", "Student_Centre_Parking",
                                  "Student_Centre", "School_of_Business", "Old_Humanities", "Cafeteria", "Main_Lab",
                                  "Cyber_Cafe", "Hostels"]),
               "Auditorium_Parking": set(["Auditorium", "Student_Centre_Parking", "Student_Centre"]),
               "Bus_Parking_Lot": set(["Basketball_Court", "Cyber_Cafe", "Cafe_Latta_Parking_Lot",
                                       "Student_Centre_Parking", "Student_Centre", "Faculty_Housing"]),
               "Faculty_Housing": set(["Cafe_Latta_Parking_Lot", "Bus_Parking_Lot", "Student_Centre_Parking"]),
               "Library": set(["Auditorium", "School_of_Business", "Old_Humanities", "Cafeteria", "Main_Lab",
                               "Library_Parking", "School_of_Science", "School_of_Science_Parking", "Hostels",
                               "Cyber_Cafe"]),
               "Library_Parking": set(["Library", "School_of_Science_Parking"]),
               "Student_Centre_Parking": set(
                   ["Faculty_Housing", "Auditorium_Parking", "Auditorium", "Student_Centre", "Bus_Parking_Lot"]),
               "Student_Centre": set(
                   ["School_of_Science", "Student_Centre_Parking", "Swimming_Pool_Parking", "Auditorium",
                    "Basketball_Court", "Auditorium_Parking", "Bus_Parking_Lot"]),
               "School_of_Science": set(
                   ["New_Humanities", "Swimming_Pool_Parking", "School_of_Science_Parking", "Student_Centre"]),
               "School_of_Science_Parking": set(
                   ["School_of_Science", "Swimming_Pool_Parking", "Library", "Library_Parking"]),
               "Swimming_Pool_Parking": set(
                   ["Swimming_Pool", "New_Humanities", "School_of_Science", "School_of_Science_Parking",
                    "Student_Centre"]),
               "Swimming_Pool": set(["Swimming_Pool_Parking"]),
               "New_Humanities": set(
                   ["School_of_Science", "School_of_Humanities_Parking_Lot", "Gate_B", "Football_Pitch",
                    "Swimming_Pool_Parking"]),
               "School_of_Humanities_Parking_Lot": set(["Gate_B", "New_Humanities"]),
               "Gate_B": set(["New_Humanities", "School_of_Humanities_Parking_Lot"]),
               "Football_Pitch": set(["New_Humanities", "Rugby_Field"]),
               "Rugby_Field": set(["Football_Pitch"])}
    cost = {str(["Gate_A", "Procurement"]): "150",
            str(["Gate_A", "Administration_Block"]): "110",
            str(["Gate_A", "Administration_Parking"]): "100",

            str(["Administration_Block", "Lillian_K_Beam"]): "25",
            str(["Administration_Block", "Gate_A"]): "110",
            str(["Administration_Block", "Administration_Parking"]): "20",
            str(["Administration_Block", "Mama_Africa"]): "20",
            str(["Administration_Block", "Transport_Office"]): "60",
            str(["Administration_Block", "Lillian_K_Beam_Parking"]): "60",  # NOT DONE

            str(["Administration_Parking", "Gate_A"]): "100",
            str(["Administration_Parking", "Transport_Office"]): "50",
            str(["Administration_Parking", "Administration_Block"]): "5",
            str(["Administration_Parking", "Lillian_K_Beam_Parking"]): "5",  # NOT DONE

            str(["Main_Lab", "Old_Humanities"]): "50",
            str(["Main_Lab", "Mama_Africa"]): "35",
            str(["Main_Lab", "Lillian_K_Beam"]): "55",
            str(["Main_Lab", "Cafeteria"]): "34",
            str(["Main_Lab", "Wooden_Blocks"]): "42",
            str(["Main_Lab", "Hostels"]): "155",
            str(["Main_Lab", "Basketball_Court"]): "200",
            str(["Main_Lab", "Library"]): "255",
            str(["Main_Lab", "Procurement"]): "30",  # NOT DONE TO DO
            str(["Main_Lab", "Auditorium"]): "210",
            str(["Main_Lab", "School_of_Business"]): "62",

            str(["Procurement", "Wooden_Blocks"]): "143",  # NOT DONE TO DO
            str(["Procurement", "Mama_Africa"]): "132",  # NOT DONE TO DO
            str(["Procurement", "Gate_A"]): "150",  # NOT DONE TO DO
            str(["Procurement", "Main_Lab"]): "30",  # NOT DONE TO DO

            str(["Mama_Africa", "Lillian_K_Beam"]): "35",
            str(["Mama_Africa", "Wooden_Blocks"]): "56",
            str(["Mama_Africa", "Procurement"]): "55",  # NOT DONE TO DO
            str(["Mama_Africa", "Administration_Block"]): "10",
            str(["Mama_Africa", "Main_Lab"]): "35",

            str(["Wooden_Blocks", "Main_Lab"]): "42",
            str(["Wooden_Blocks", "Procurement"]): "20",  # NOT DONE TO DO
            str(["Wooden_Blocks", "Cafeteria"]): "45",
            str(["Wooden_Blocks", "Mama_Africa"]): "56",
            str(["Wooden_Blocks", "Old_Humanities"]): "20",

            str(["Lillian_K_Beam", "Cafeteria"]): "35",
            str(["Lillian_K_Beam", "Administration_Block"]): "30",
            str(["Lillian_K_Beam", "Main_Lab"]): "55",
            str(["Lillian_K_Beam", "Mama_Africa"]): "55",
            str(["Lillian_K_Beam", "Lillian_K_Beam_Parking"]): "55",  # NOT DONE

            str(["Cafeteria", "Lillian_K_Beam"]): "35",
            str(["Cafeteria", "Wooden_Blocks"]): "45",
            str(["Cafeteria", "Main_Lab"]): "34",
            str(["Cafeteria", "Hostels"]): "49",
            str(["Cafeteria", "Library"]): "125",
            str(["Cafeteria", "Auditorium"]): "110",
            str(["Cafeteria", "School_of_Business"]): "126",
            str(["Cafeteria", "Old_Humanities"]): "146",
            str(["Cafeteria", "Transport_Office"]): "26",
            str(["Cafeteria", "Basketball_Court"]): "78",
            str(["Cafeteria", "Lillian_K_Beam_Parking"]): "78",  # NOT DONE

            str(["Old_Humanities", "Wooden_Blocks"]): "24",
            str(["Old_Humanities", "School_of_Business"]): "32",
            str(["Old_Humanities", "Main_Lab"]): "22",
            str(["Old_Humanities", "Auditorium"]): "123",
            str(["Old_Humanities", "Library"]): "110",
            str(["Old_Humanities", "Cafeteria"]): "146",
            str(["Old_Humanities", "Hostels"]): "132",
            str(["Old_Humanities", "Basketball_Court"]): "155",

            str(["School_of_Business", "Old_Humanities"]): "32",
            str(["School_of_Business", "Main_Lab"]): "62",
            str(["School_of_Business", "Auditorium"]): "44",
            str(["School_of_Business", "Library"]): "57",
            str(["School_of_Business", "Cafeteria"]): "126",
            str(["School_of_Business", "Hostels"]): "136",
            str(["School_of_Business", "Basketball_Court"]): "172",

            str(["Hostels", "Cafeteria"]): "49",
            str(["Hostels", "Cafe_Latta"]): "10",
            str(["Hostels", "School_of_Business"]): "136",
            str(["Hostels", "Auditorium"]): "80",
            str(["Hostels", "Library"]): "125",
            str(["Hostels", "Old_Humanities"]): "132",
            str(["Hostels", "Main_Lab"]): "155",
            str(["Hostels", "Transport_Office"]): "15",
            str(["Hostels", "Basketball_Court"]): "75",

            str(["Cyber_Cafe", "Cafe_Latta"]): "5",
            str(["Cyber_Cafe", "Auditorium"]): "85",
            str(["Cyber_Cafe", "Library"]): "120",
            str(["Cyber_Cafe", "Basketball_Court"]): "95",
            str(["Cyber_Cafe", "Bus_Parking_Lot"]): "25",  # Not done

            str(["Transport_Office", "Cafe_Latta"]): "18",
            str(["Transport_Office", "Hostels"]): "15",
            str(["Transport_Office", "Administration_Parking"]): "20",
            str(["Transport_Office", "Cafeteria"]): "20",
            str(["Transport_Office", "Administration_Block"]): "40",
            str(["Transport_Office", "Cafe_Latta_Parking_Lot"]): "35",

            str(["Cafe_Latta", "Cafe_Latta_Parking_Lot"]): "10",
            str(["Cafe_Latta", "Hostels"]): "10",
            str(["Cafe_Latta", "Transport_Office"]): "18",
            str(["Cafe_Latta", "Bus_Parking_Lot"]): "26",
            str(["Cafe_Latta", "Cyber_Cafe"]): "5",

            str(["Cafe_Latta_Parking_Lot", "Bus_Parking_Lot"]): "4",
            str(["Cafe_Latta_Parking_Lot", "Cafe_Latta"]): "5",
            str(["Cafe_Latta_Parking_Lot", "Faculty_Housing"]): "20",
            str(["Cafe_Latta_Parking_Lot", "Student_Centre_Parking"]): "110",
            str(["Cafe_Latta_Parking_Lot", "Hostels"]): "15",
            str(["Cafe_Latta_Parking_Lot", "Transport_Office"]): "35",

            str(["Basketball_Court", "Cyber_Cafe"]): "95",
            str(["Basketball_Court", "Bus_Parking_Lot"]): "30",
            str(["Basketball_Court", "Auditorium"]): "16",
            str(["Basketball_Court", "Library"]): "112",
            str(["Basketball_Court", "School_of_Business"]): "160",
            str(["Basketball_Court", "Old_Humanities"]): "155",
            str(["Basketball_Court", "Cafeteria"]): "130",
            str(["Basketball_Court", "Student_Centre_Parking"]): "40",
            str(["Basketball_Court", "Student_Centre"]): "120",
            str(["Basketball_Court", "Main_Lab"]): "138",
            str(["Basketball_Court", "Hostels"]): "40",

            str(["Auditorium", "Basketball_Court"]): "16",
            str(["Auditorium", "Library"]): "70",
            str(["Auditorium", "Auditorium_Parking"]): "10",
            str(["Auditorium", "Student_Centre_Parking"]): "50",
            str(["Auditorium", "Student_Centre"]): "130",
            str(["Auditorium", "School_of_Business"]): "80",
            str(["Auditorium", "Old_Humanities"]): "123",
            str(["Auditorium", "Cafeteria"]): "110",
            str(["Auditorium", "Main_Lab"]): "210",
            str(["Auditorium", "Cyber_Cafe"]): "85",
            str(["Auditorium", "Hostels"]): "80",

            str(["Auditorium_Parking", "Auditorium"]): "10",
            str(["Auditorium_Parking", "Student_Centre_Parking"]): "40",
            str(["Auditorium_Parking", "Student_Centre"]): "120",

            str(["Bus_Parking_Lot", "Basketball_Court"]): "30",
            str(["Bus_Parking_Lot", "Cyber_Cafe"]): "75",
            str(["Bus_Parking_Lot", "Cafe_Latta_Parking_Lot"]): "5",
            str(["Bus_Parking_Lot", "Student_Centre_Parking"]): "75",
            str(["Bus_Parking_Lot", "Student_Centre"]): "175",
            str(["Bus_Parking_Lot", "Faculty_Housing"]): "35",

            str(["Faculty_Housing", "Cafe_Latta_Parking_Lot"]): "10",
            str(["Faculty_Housing", "Bus_Parking_Lot"]): "15",
            str(["Faculty_Housing", "Student_Centre_Parking"]): "80",

            str(["Library", "Auditorium"]): "70",
            str(["Library", "School_of_Business"]): "95",
            str(["Library", "Old_Humanities"]): "110",
            str(["Library", "Cafeteria"]): "125",
            str(["Library", "Main_Lab"]): "255",
            str(["Library", "Library_Parking"]): "60",
            str(["Library", "School_of_Science"]): "230",
            str(["Library", "School_of_Science_Parking"]): "210",
            str(["Library", "Hostels"]): "110",
            str(["Library", "Cyber_Cafe"]): "115",

            str(["Library_Parking", "Library"]): "70",
            str(["Library_Parking", "School_of_Science_Parking"]): "170",

            str(["Student_Centre_Parking", "Faculty_Housing"]): "80",
            str(["Student_Centre_Parking", "Auditorium_Parking"]): "40",
            str(["Student_Centre_Parking", "Auditorium"]): "50",
            str(["Student_Centre_Parking", "Student_Centre"]): "40",
            str(["Student_Centre_Parking", "Bus_Parking_Lot"]): "60",

            str(["Student_Centre", "School_of_Science"]): "86",
            str(["Student_Centre", "Student_Centre_Parking"]): "40",
            str(["Student_Centre", "Swimming_Pool_Parking"]): "50",
            str(["Student_Centre", "Auditorium"]): "130",
            str(["Student_Centre", "Basketball_Court"]): "120",
            str(["Student_Centre", "Auditorium_Parking"]): "70",
            str(["Student_Centre", "Bus_Parking_Lot"]): "120",

            str(["School_of_Science", "New_Humanities"]): "90",
            str(["School_of_Science", "Swimming_Pool_Parking"]): "50",
            str(["School_of_Science", "School_of_Science_Parking"]): "21",
            str(["School_of_Science", "Student_Centre"]): "80",

            str(["School_of_Science_Parking", "School_of_Science"]): "21",
            str(["School_of_Science_Parking", "Swimming_Pool_Parking"]): "30",
            str(["School_of_Science_Parking", "Library"]): "180",
            str(["School_of_Science_Parking", "Library_Parking"]): "120",

            str(["Swimming_Pool_Parking", "Swimming_Pool"]): "5",
            str(["Swimming_Pool_Parking", "New_Humanities"]): "95",
            str(["Swimming_Pool_Parking", "School_of_Science"]): "55",
            str(["Swimming_Pool_Parking", "Student_Centre"]): "20",
            str(["Swimming_Pool_Parking", "School_of_Science_Parking"]): "30",

            str(["Swimming_Pool", "Swimming_Pool_Parking"]): "5",

            str(["New_Humanities", "School_of_Science"]): "90",
            str(["New_Humanities", "School_of_Humanities_Parking_Lot"]): "120",
            str(["New_Humanities", "Gate_B"]): "150",
            str(["New_Humanities", "Football_Pitch"]): "230",
            str(["New_Humanities", "Swimming_Pool_Parking"]): "80",

            str(["School_of_Humanities_Parking_Lot", "Gate_B"]): "30",
            str(["School_of_Humanities_Parking_Lot", "New_Humanities"]): "120",

            str(["Gate_B", "New_Humanities"]): "150",
            str(["Gate_B", "School_of_Humanities_Parking_Lot"]): "30",

            str(["Football_Pitch", "New_Humanities"]): "230",
            str(["Football_Pitch", "Rugby_Field"]): "100",

            str(["Rugby_Field", "Football_Pitch"]): "100",

            str(["Lillian_K_Beam_Parking", "Lillian_K_Beam"]): "55",  # NOT DONE
            str(["Lillian_K_Beam_Parking", "Administration_Block"]): "35",  # NOT DONE
            str(["Lillian_K_Beam_Parking", "Administration_Parking"]): "55",  # NOT DONE
            str(["Lillian_K_Beam_Parking", "Cafeteria"]): "55",  # NOT DONE
            }
    DriveCost = {str(["Gate_A", "Administration_Parking"]): "110",

                 str(["Administration_Parking", "Gate_A"]): "110",
                 str(["Administration_Parking", "Bus_Parking_Lot"]): "220",
                 str(["Administration_Parking", "Cafe_Latta_Parking_Lot"]): "230",
                 str(["Administration_Parking", "Lillian_K_Beam_Parking"]): "120",

                 str(["Lillian_K_Beam_Parking", "Administration_Parking"]): "70",
                 str(["Lillian_K_Beam_Parking", "Cafe_Latta_Parking_Lot"]): "280",
                 str(["Lillian_K_Beam_Parking", "Bus_Parking_Lot"]): "295",

                 str(["Cafe_Latta_Parking_Lot", "Administration_Parking"]): "230",
                 str(["Cafe_Latta_Parking_Lot", "Lillian_K_Beam_Parking"]): "280",
                 str(["Cafe_Latta_Parking_Lot", "Bus_Parking_Lot"]): "55",
                 str(["Cafe_Latta_Parking_Lot", "Student_Centre_Parking"]): "300",
                 str(["Cafe_Latta_Parking_Lot", "Auditorium_Parking"]): "150",

                 str(["Bus_Parking_Lot", "Administration_Parking"]): "220",
                 str(["Bus_Parking_Lot", "Lillian_K_Beam_Parking"]): "240",
                 str(["Bus_Parking_Lot", "Cafe_Latta_Parking_Lot"]): "55",
                 str(["Bus_Parking_Lot", "Student_Centre_Parking"]): "170",
                 str(["Bus_Parking_Lot", "Auditorium_Parking"]): "135",

                 str(["Student_Centre_Parking", "Cafe_Latta_Parking_Lot"]): "180",
                 str(["Student_Centre_Parking", "Swimming_Pool_Parking"]): "140",
                 str(["Student_Centre_Parking", "Auditorium_Parking"]): "130",
                 str(["Student_Centre_Parking", "Bus_Parking_Lot"]): "135",

                 str(["Auditorium_Parking", "Cafe_Latta_Parking_Lot"]): "180",
                 str(["Auditorium_Parking", "Swimming_Pool_Parking"]): "150",
                 str(["Auditorium_Parking", "Student_Centre_Parking"]): "130",
                 str(["Auditorium_Parking", "Bus_Parking_Lot"]): "135",

                 str(["Swimming_Pool_Parking", "School_of_Humanities_Parking_Lot"]): "300",
                 str(["Swimming_Pool_Parking", "Auditorium_Parking"]): "150",
                 str(["Swimming_Pool_Parking", "Student_Centre_Parking"]): "140",
                 str(["Swimming_Pool_Parking", "School_of_Science_Parking"]): "130",

                 str(["School_of_Science_Parking", "Library_Parking"]): "150",
                 str(["School_of_Science_Parking", "Swimming_Pool_Parking"]): "130",

                 str(["Library_Parking", "School_of_Science_Parking"]): "150",

                 str(["School_of_Humanities_Parking_Lot", "Swimming_Pool_Parking"]): "300",
                 str(["School_of_Humanities_Parking_Lot", "Gate_B"]): "75",

                 str(["Gate_B", "School_of_Humanities_Parking_Lot"]): "75",

                 }

    Drive = {"Gate_A": set(["Administration_Parking"]),
             "Administration_Parking": set(
                 ["Gate_A", "Cafe_Latta_Parking_Lot", "Bus_Parking_Lot", "Lillian_K_Beam_Parking"]),
             "Lillian_K_Beam_Parking": set(["Administration_Parking", "Cafe_Latta_Parking_Lot", "Bus_Parking_Lot"]),
             "Cafe_Latta_Parking_Lot": set(
                 ["Administration_Parking", "Bus_Parking_Lot", "Student_Centre_Parking", "Auditorium_Parking"]),
             "Bus_Parking_Lot": set(
                 ["Administration_Parking", "Cafe_Latta_Parking_Lot", "Student_Centre_Parking", "Auditorium_Parking"]),
             "Student_Centre_Parking": set(
                 ["Cafe_Latta_Parking_Lot", "Bus_Parking_Lot", "Auditorium_Parking", "Swimming_Pool_Parking"]),
             "Auditorium_Parking": set(
                 ["Cafe_Latta_Parking_Lot", "Bus_Parking_Lot", "Student_Centre_Parking", "Swimming_Pool_Parking"]),
             "Swimming_Pool_Parking": set(
                 ["Auditorium_Parking", "Student_Centre_Parking", "School_of_Humanities_Parking_Lot",
                  "School_of_Science_Parking"]),
             "School_of_Science_Parking": set(["Library_Parking", "Swimming_Pool_Parking"]),
             "Library_Parking": set(["School_of_Science_Parking"]),
             "School_of_Humanities_Parking_Lot": set(["Swimming_Pool_Parking", "Gate_B"]),
             "Gate_B": set(["School_of_Humanities_Parking_Lot"])

             }

    myDriveHeuristic = {"Administration_Parking": ["160", "40"],
                        "Cafe_Latta_Parking_Lot": ["74", "134"],
                        "Auditorium_Parking": ["130", "224"],
                        "Bus_Parking_Lot": ["94", "152"],
                        "Student_Centre_Parking": ["74", "220"],
                        "Library_Parking": ["210", "224"],
                        "School_of_Science_Parking": ["164", "284"],
                        "Swimming_Pool_Parking": ["100", "284"],
                        "School_of_Humanities_Parking_Lot": ["204", "394"],
                        "Lillian_K_Beam_Parking": ["180", "72"],
                        }
    myheuristic = {"Gate_A": ["210", "4"],
                   "Administration_Block": ["186", "50"],
                   "Administration_Parking": ["160", "40"],
                   "Lillian_K_Beam": ["190", "72"],
                   "Lillian_K_Beam_Parking": ["180", "72"],
                   "Cafeteria": ["160", "90"],
                   "Main_Lab": ["218", "80"],
                   "Procurement": ["240", "80"],
                   "Mama_Africa": ["203", "50"],
                   "Wooden_Blocks": ["234", "94"],
                   "Old_Humanities": ["228", "121"],
                   "School_of_Business": ["220", "148"],
                   "Hostels": ["132", "110"],
                   "Cyber_Cafe": ["114", "142"],
                   "Transport_Office": ["136", "70"],
                   "Cafe_Latta": ["102", "134"],
                   "Cafe_Latta_Parking_Lot": ["74", "134"],
                   "Basketball_Court": ["100", "174"],
                   "Auditorium": ["140", "192"],
                   "Auditorium_Parking": ["130", "224"],
                   "Bus_Parking_Lot": ["94", "152"],
                   "Faculty_Housing": ["62", "174"],
                   "Library": ["178", "222"],
                   "Library_Parking": ["210", "224"],
                   "Student_Centre_Parking": ["74", "220"],
                   "Student_Centre": ["98", "274"],
                   "School_of_Science": ["170", "310"],
                   "School_of_Science_Parking": ["164", "284"],
                   "Swimming_Pool_Parking": ["100", "284"],
                   "Swimming_Pool": ["100", "320"],
                   "New_Humanities": ["162", "368"],
                   "School_of_Humanities_Parking_Lot": ["204", "394"],
                   "Gate_B": ["284", "400"],
                   "Football_Pitch": ["260", "655"],
                   "Rugby_Field": ["314", "595"],

                   }

    start = "School_of_Science_Parking"
    goal = "Basketball_Court"


class Agent(Environment):
    def getCost(pathtoCost, cost):
        pathCost = 0
        i = 0
        while i < len(pathtoCost) - 1:
            l = []
            l.append(pathtoCost[i])
            l.append(pathtoCost[i + 1])
            pathCost = pathCost + int(cost[str(l)])  # Read the cost between the nodes
            i += 1
        return pathCost

    def getH(vertex, goal):
        v = []
        g = []

        # reading the axis

        for i in Environment.myheuristic[vertex]:
            v.append(int(i))  # convert to int to use in calc

        # reading coord of dest:
        for i in Environment.myheuristic[goal]:
            g.append(int(i))  # convert to int to use in calc

        heuristics = abs(v[0] - g[0]) + abs(v[1] - g[1])  # modulus mod(x1-x2) + mod(y1-y2)
        return heuristics

    def driveH(goal):
        y = 10000
        destination = ""
        for i in Environment.myDriveHeuristic:
            x = (abs(int(Environment.myheuristic[i][0]) - int(Environment.myheuristic[goal][0])))
            z = (abs(int(Environment.myheuristic[i][1]) - int(Environment.myheuristic[goal][1])))

            if ((x + z) < y):
                y = abs(x + z)
                destination = i
        return destination

    def DriveAstar(graph, start, goal):
        p = []  # hosts path
        k = []
        p.append(start)
        destination = Agent.driveH(goal)
        print(destination)

        # infinite loop
        while True:
            # what is next to start position:
            neighbour = graph[start]  # graph contains neighbour of any node
            h = {}
            for i in neighbour.difference(p):  # go to all neighbours escept those visisted.
                l = []
                l.append(str(start))
                l.append(str(i))  # neighbour
                h[i] = Agent.getH(i, destination) + Agent.getCost(l, Environment.DriveCost)  # calc huristics
                print("hi",h)

            # best huristic from list, then pick first item:
            sortedH = sorted(h.items(), key=operator.itemgetter(1))
            x = next(iter(sortedH[0]))  # contains the best huristics
            p.append(x)

            if x == destination:
                print("walk now")
                print(x, goal)
                k = Agent.Astar(Environment.myGraph, x, goal)

                return p, "           now walk             ", k
            else:
                start = x

    def Astar(graph, start, goal):
        p = []  # hosts path
        p.append(start)

        # infinite loop
        while True:
            # what is next to start position:
            neighbour = graph[start]  # graph contains neighbour of any node
            h = {}
            for i in neighbour.difference(p):  # go to all neighbours escept those visisted.
                l = []
                l.append(str(start))
                l.append(str(i))  # neighbour
                h[i] = Agent.getH(i, goal) + Agent.getCost(l, Environment.cost)  # calc huristics

            # best huristic from list, then pick first item:
            sortedH = sorted(h.items(), key=operator.itemgetter(1))
            x = next(iter(sortedH[0]))  # contains the best huristics
            p.append(x)

            if x == goal:
                return p
            else:
                start = x

    def GBFS(graph, start, goal):
        p = []  # hosts path
        p.append(start)

        # infinite loop
        while True:
            # what is next to start position:
            neighbour = graph[start]  # graph contains neighbour of any node
            h = {}
            for i in neighbour.difference(p):  # go to all neighbours escept those visisted.
                h[i] = Agent.getH(i, goal)  # calc huristics

            # best huristic from list, then pick first item:
            sortedH = sorted(h.items(), key=operator.itemgetter(1))
            x = next(iter(sortedH[0]))  # contains the best huristics
            p.append(x)

            if x == goal:
                return p

            else:
                start = x

    def multiDest(graph, start, g1, g2):
        y = Agent.Astar(graph, start, g1)
        z = Agent.Astar(graph, g1, g2)

        print(y)
        print(z)
        return y, "     end     ", z

    def displayGUI(myGraph, myDrive):
        location = []
        for value in myGraph:
            location.append(value)  # used to store all locations of walking in a drop-down list
        location0 = ["Walking", "Driving", "Parking For Disabled","MultiDestination"]
        location10 = []
        for value in myDrive:
            location10.append(value)

        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
        app = customtkinter.CTk()  # create CTk window like you do with the Tk window
        app.geometry("1900x500")
        app.title("USIU-A AI MAP")
        # Use CTkButton instead of tkinter Button
        label0 = customtkinter.CTkLabel(master=app, text="Please enter if you are walking or driving: \n")
        label0.pack()
        clicked0 = customtkinter.StringVar(value="Walking")
        drop0 = customtkinter.CTkOptionMenu(master=app, values=location0,variable=clicked0)
        drop0.pack()
        
        #button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        def getDirection(app, location, myGraph, clicked):
            customtkinter.set_default_color_theme("green")
            if (clicked0.get() == "Driving"):
                drop = customtkinter.CTkOptionMenu(master=app, variable=clicked, values=location10)
                drop.pack()
            else:
                drop = customtkinter.CTkOptionMenu(master=app, variable=clicked, values=location)
                drop.pack()
            label2 = customtkinter.CTkLabel(master=app, text="Please enter the place you want to be at: ")
            label2.pack()
            clicked2 = customtkinter.StringVar(value="Gate_A")

            drop2 = customtkinter.CTkOptionMenu(master=app, variable=clicked2, values=location)
            drop2.pack()
            label3 = customtkinter.CTkLabel(master=app, text=" ")
            label3.pack()
            if(clicked0.get() == "MultiDestination"):
                label5 = customtkinter.CTkLabel(master=app, text="Enter the Third location")
                label5.pack()
                clicked3 = customtkinter.StringVar(value="Gate_A")
                drop3 = customtkinter.CTkOptionMenu(master=app, variable=clicked3, values=location)
                drop3.pack()

            def results():
                if (clicked.get() == clicked2.get()):
                    label4 = customtkinter.CTkLabel(master=app,text="Please do not enter the same location in both fields. \n").pack()
                elif (clicked0.get() == "Parking For Disabled"):
                    x = str(Agent.Astar(Environment.myGraph, clicked.get(), clicked2.get()))
                    y = str(Agent.GBFS(Environment.myGraph, clicked.get(), clicked2.get()))
                    label4 = customtkinter.CTkLabel(master=app,text="Follow this route to get to your destination when driving: " + x + "\n").pack()
                    if x != y:
                        label6 = customtkinter.CTkLabel(master=app,text="For an alternate route: " + y + "\n").pack()
                elif(clicked0.get() == "Walking"):
                    x = str(Agent.Astar(Environment.myGraph, clicked.get(), clicked2.get()))
                    y = str(Agent.GBFS(Environment.myGraph, clicked.get(), clicked2.get()))
                    label4 = customtkinter.CTkLabel(master=app, text="Follow this route to get to your destination when driving: " + x + "\n").pack()
                    if x != y:
                        label6 = customtkinter.CTkLabel(master=app, text="For an alternate route: " + y + "\n").pack()
                elif (clicked0.get() == "Driving"):
                    x=str(Agent.DriveAstar(Environment.Drive, clicked.get(), clicked2.get()))
                    label4 = customtkinter.CTkLabel(master=app, text="Follow this route to get to your destination when driving: " + x + "\n").pack()
                else:
                    label4 = customtkinter.CTkLabel(master=app, text="Follow this route to get to your destination when driving: " + str(
                        Agent.multiDest(Environment.myGraph, clicked.get(), clicked2.get(),clicked3.get())) + "\n").pack()

#            customtkinter.set_default_color_theme("blue")
 #           button = customtkinter.CTkButton(master=app, text="Generate Distances", command=chooseDistance)
  #          button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

            customtkinter.set_default_color_theme("blue")
            button = customtkinter.CTkButton(master=app, text="Get Direction", command=results).pack()
            label7 = customtkinter.CTkLabel(master=app, text=" \n").pack()
            customtkinter.CTkButton(master=app, text="QUIT", command=app.destroy).pack()
            label8 = customtkinter.CTkLabel(master=app, text=" \n").pack()
            return

        def chooseDistance():
            label = customtkinter.CTkLabel(master=app, text="\nPlease enter the place you are at: ")
            label.pack()
            clicked = customtkinter.StringVar(value="Gate_A")
            if (clicked0.get() == "Walking"):
                getDirection(app, location, myGraph, clicked)
            elif (clicked0.get() == "Parking For Disabled"):
                getDirection(app, location10, myDrive, clicked)
            elif(clicked0.get() == "Driving"):
                getDirection(app, location, myGraph, clicked)
            else:
                getDirection(app, location, myGraph, clicked)

        customtkinter.set_default_color_theme("blue")
        button = customtkinter.CTkButton(master=app, text="Generate Distances", command=chooseDistance)
        button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        app.mainloop()

    def __init__(self, Environment):
        Agent.displayGUI(Environment.myGraph, Environment.Drive)
        # print("DFS", Agent.DFS(Environment.myGraph, Environment.start, Environment.goal))
        # print("BFS", Agent.BFS(Environment.myGraph, Environment.start, Environment.goal))
        # print("UCS", Agent.UCS(Environment.myGraph, Environment.start, Environment.goal))
        # print("GBFS", Agent.GBFS(Environment.myGraph, Environment.start, Environment.goal))
        # print("A *", Agent.Astar(Environment.myGraph, "Administration_Parking", Environment.goal))
        print("DriveA *", Agent.DriveAstar(Environment.Drive, Environment.start, Environment.goal))
        print("MultiDest *",Agent.multiDest(Environment.myGraph, Environment.start, Environment.goal, "Lillian_K_Beam"))
        # print("Hill CLimbing", Agent.hillclimbing(Environment.myGraph, Environment.start, Environment.goal))

       
theEnvironment = Environment()
theagent = Agent(theEnvironment)