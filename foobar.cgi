#!/usr/bin/env jshell-cgi-wrapper


import com.google.gson.GsonBuilder;
import com.google.gson.Gson;

class Employee {
 private String name;
    Employee(String name) {
       this.name=name;
    }
    String getName() {
       return name;
    }
    void setName(String name) {
       this.name=name;
    }
 }

Gson g = new GsonBuilder().setPrettyPrinting().create();
Employee emp = new Employee("Deivid Germano Silva Santos")
String empSerialized = g.toJson(emp);
System.out.println(empSerialized);