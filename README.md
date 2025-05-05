# LibraryManagementSystem
Library mangement system made in python using Tkinter and mysql as database

to run this program one must have mysql workbench and have a database named "project" and it must have table called "library"

the table must have the columns

Member, PRN_NO, ID, FirstName, LastName, Address1, Address2, PostId, Mobile, BookId, BookTitle, Auther, Dateborrowed, DateDue, Daysonbook, LateReturnFine, Daysoverdue, finalPrice

Run the following command on your mysql workbench

CREATE DATABASE project;
CREATE TABLE library (
Member varchar(50),
PRN_NO varchar(50),
ID varchar(50),
FirstName varchar(50),
LastName varchar(50),
Address1 varchar(50),
Address2 varchar(50), PostId varchar(50),
Mobile varchar(50),
BookId varchar(50),
BookTitle varchar(50),
Auther varchar(50),
Dateborrowed varchar(50),
DateDue varchar(50),
Daysonbook varchar(50),
LateReturnFine varchar(50),
Daysoverdue varchar(50),
finalPrice varchar(50)
);



The end
