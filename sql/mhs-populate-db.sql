
-- Populate facilities
INSERT INTO `facility` (`FacID`, `Name`, `Address`, `City`, `State`, `Zip`, `Size`, `FType`) VALUES
(1, 'Anytown General Hospital', '1 Main St', 'Anytown', 'CA', '54321', 100, 'OPS'),
(2, 'Anytown Urgent Care', '5 Main St', 'Anytown', 'CA', '54321', 500, 'OPS'),
(3, 'Anytown Medical Office', '6 Main St', 'Anytown', 'CA', '54321', 200, 'Office');

-- Populate facility types
INSERT INTO `ops` (`FacID`, `Room_Count`, `P_code`, `Description`) VALUES
(1, 20, 'ER', 'Emergency Room'),
(2, 10, 'UC', 'Urgent Care Treatment Rooms');

INSERT INTO `office` (`FacID`, `Office_Count`) VALUES
(3, 15);



-- Populate employees
INSERT INTO `employee` (`EmpID`, `FName`, `Minit`, `LName`, `Street`, `City`, `State`, `Zip`, `FacID`, `JobClass`, `SSN`, `Salary`, `HireDate`) VALUES
(1, 'John', 'A', 'Doe', '123 Main St', 'Anytown', 'CA', '12345', 1, 'Doctor', 123456789, '100000.00', '2023-01-01'),
(2, 'Jane', 'B', 'Smith', '456 Elm St', 'Anytown', 'CA', '54321', 2, 'Nurse', 987654321, '80000.00', '2024-01-01'),
(3, 'David', 'C', 'Lee', '789 Maple St', 'Anytown', 'CA', '98765', 2, 'Other HCP', 246801357, '70000.00', '2022-01-01'),
(4, 'Samantha', 'D', 'Kacpersky', '555 Some Rd', 'Anytown', 'CA', '54321', 3, 'Admin', 246801354, '70000.00', '2020-01-01'),
(5, 'Jake', 'E', 'Doe', '123 Main St', 'Anytown', 'CA', '12345', 2, 'Doctor', 123456788, '100000.00', '2023-01-01'),
(6, 'Jannette', 'F', 'Smith', '456 Elm St', 'Anytown', 'CA', '54321', 1, 'Nurse', 987654320, '80000.00', '2024-01-01'),
(7, 'Dennis', 'G', 'Lee', '789 Maple St', 'Anytown', 'CA', '98765', 1, 'Other HCP', 246801356, '70000.00', '2022-01-01'),
(8, 'Sally', 'H', 'Kacpersky', '555 Some Rd', 'Anytown', 'CA', '54321', 3, 'Admin', 246801355, '70000.00', '2020-01-01');

-- Populate employee jobclasses
INSERT INTO `doctor` (`EmpID`, `Speciality`, `BC_Date`) VALUES
(1, 'Cardiology', '2010-01-01'),
(5, 'Pediatrics', '2016-01-01');

INSERT INTO `nurse` (`EmpID`, `Certification`) VALUES
(2, 'RN'),
(6, 'RN');

INSERT INTO `otherhcp` (`EmpID`, `JobTitle`) VALUES
(3, 'Physical Therapist'),
(7, 'Chiropractor');

INSERT INTO `admin` (`EmpID`, `JobTitle`) VALUES
(4, 'Chief of Staff'),
(8, 'Chief of Surgery');



-- Populate insurance companies
INSERT INTO `insurancecompany` (`Ins_id`, `Name`, `Street`, `City`, `State`, `Zip`) VALUES
(1, 'Aetna', '1 Main St', 'Anytown', 'CA', '12345'),
(2, 'Blue Cross Blue Shield', '5 Main St', 'Anytown', 'CA', '54321');



-- Populate patients
INSERT INTO `patient` (`P_id`, `FName`, `Minit`, `LName`, `Street`, `City`, `State`, `Zip`, `Ins_id`, `PrimaryDoctorID`) VALUES
(1, 'Alice', 'A', 'Brown', '123 Main St', 'Anytown', 'CA', '12345', 1, 1),
(2, 'Bob', 'B', 'Jones', '456 Elm St', 'Anytown', 'CA', '54321', 2, 5),
(3, 'Arnold', 'C', 'Smith', '777 Oak Rd', 'Anytown', 'CA', '65432', 2, 1),
(4, 'Hein', 'D', 'Kim', '555 Willow Ave', 'Anytown', 'CA', '99999', 1, 5),
(5, 'Ann', 'E', 'Brown', '123 Main St', 'Anytown', 'CA', '12345', 1, 1),
(6, 'Bernard', 'F', 'Jones', '456 Elm St', 'Anytown', 'CA', '54321', 2, 5),
(7, 'Alfred', 'G', 'Smith', '777 Oak Rd', 'Anytown', 'CA', '65432', 2, 1),
(8, 'Renjie', 'H', 'Liu', '555 Willow Ave', 'Anytown', 'CA', '99999', 1, 5);

-- Populate doctor treats patient
INSERT INTO `doctortreatspatient` (`Doctor_ID`, `P_id`) VALUES
(1, 2),
(5, 3);

-- Populate makes appointment
INSERT INTO `makesappointment` (`Doctor_ID`, `P_id`, `Date_Time`, `FacID`, `Description`) VALUES
(1, 1, '2024-05-10 10:00:00', 1, 'Cardiology Consultation'),
(5, 2, '2024-05-15 14:00:00', 2, 'Physical Therapy Session');
