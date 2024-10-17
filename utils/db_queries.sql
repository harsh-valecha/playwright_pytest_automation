select * from users;


insert into users(username,password) values('John Doe','ThisIsNotAPassword');

CREATE TABLE [new_table] ( 
  [id] INTEGER PRIMARY KEY AUTOINCREMENT,
  [facility] VARCHAR(250) NOT NULL,
  [apply_for_hospital_readmission] INT NULL DEFAULT 0 ,
  [healthcare_program] TEXT CHECK(healthcare_program IN ('Medicare', 'Medicaid', 'None')) NOT NULL,
  [visit_date] DATETIME NOT NULL,
  [comment] VARCHAR(250) NULL,
  [booking_timestamp] DATETIME NULL DEFAULT CURRENT_TIMESTAMP 
);

select * from form_data;

INSERT INTO form_data (facility, apply_for_hospital_readmission, healthcare_program, visit_date, comment)
VALUES ('Tokyo CURA Healthcare Center', 1, 'Medicare', '2024-10-20', 'Routine checkup');

INSERT INTO form_data (facility, apply_for_hospital_readmission, healthcare_program, visit_date, comment)
VALUES ('Hong Kong CURA Healthcare Center', 0, 'Medicaid', '2024-11-05', 'Follow-up for surgery');

INSERT INTO Appointments (facility, apply_for_hospital_readmission, healthcare_program, visit_date, comment)
VALUES ('Seoul CURA Healthcare Center', 0, 'None', '2024-12-15', 'First-time consultation');

INSERT INTO form_data(facility, apply_for_hospital_readmission, healthcare_program, visit_date, comment)
VALUES ('Tokyo CURA Healthcare Center', 1, 'Medicare', '2024-11-22', 'Post-discharge appointment');

INSERT INTO form_data(facility, apply_for_hospital_readmission, healthcare_program, visit_date, comment)
VALUES ('Berlin CURA Healthcare Center', 0, 'Medicaid', '2024-10-25', 'General wellness check');

INSERT INTO form_data(facility, apply_for_hospital_readmission, healthcare_program, visit_date, comment)
VALUES ('New York CURA Healthcare Center', 0, 'None', '2024-12-01', 'Routine health screening');


SELECT strftime('%d/%m/%Y', booking_timestamp) AS formatted_date
FROM form_data;

select users.username , users.password , form_data.facility , 
form_data.apply_for_hospital_readmission , form_data.healthcare_program , 
strftime('%d/%m/%Y', form_data.visit_date ), form_data.comment --, booking_timestamp
from users cross join form_data;

UPDATE form_data 
SET facility = 'Seoul CURA Healthcare Center' 
WHERE facility = 'New York CURA Healthcare Center';

UPDATE form_data 
SET booking_timestamp = DATE(booking_timestamp);




