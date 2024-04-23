-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               11.3.2-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for mhs
DROP DATABASE IF EXISTS `mhs`;
CREATE DATABASE `mhs` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `mhs`;

-- Dumping structure for table mhs.employee
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `EmpID` int(11) NOT NULL AUTO_INCREMENT,
  `FName` varchar(50) NOT NULL,
  `Minit` varchar(50) NOT NULL,
  `LName` varchar(50) NOT NULL,
  `Street` varchar(50) NOT NULL,
  `City` varchar(50) NOT NULL,
  `State` varchar(50) NOT NULL,
  `Zip` varchar(50) NOT NULL,
  `FacID` int(11) NOT NULL,
  `JobClass` varchar(50) NOT NULL,
  `SSN` int(11) NOT NULL,
  `Salary` varchar(50) NOT NULL,
  `HireDate` date NOT NULL,
  PRIMARY KEY (`EmpID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping structure for table mhs.admin
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `EmpID` int(11) NOT NULL,
  `JobTitle` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`EmpID`),
  CONSTRAINT `FK_admin_employee` FOREIGN KEY (`EmpID`) REFERENCES `employee` (`EmpID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping structure for table mhs.doctor
DROP TABLE IF EXISTS `doctor`;
CREATE TABLE `doctor` (
  `EmpID` int(11) NOT NULL,
  `Speciality` varchar(50) DEFAULT NULL,
  `BC_Date` date DEFAULT NULL,
  PRIMARY KEY (`EmpID`),
  CONSTRAINT `FK_doctor_employee` FOREIGN KEY (`EmpID`) REFERENCES `employee` (`EmpID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping structure for table mhs.nurse
DROP TABLE IF EXISTS `nurse`;
CREATE TABLE `nurse` (
  `EmpID` int(11) NOT NULL,
  `Certification` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`EmpID`),
  CONSTRAINT `FK_nurse_employee` FOREIGN KEY (`EmpID`) REFERENCES `employee` (`EmpID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping structure for table mhs.otherhcp
DROP TABLE IF EXISTS `otherhcp`;
CREATE TABLE `otherhcp` (
  `EmpID` int(11) NOT NULL,
  `JobTitle` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`EmpID`),
  CONSTRAINT `FK_otherhcp_employee` FOREIGN KEY (`EmpID`) REFERENCES `employee` (`EmpID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping structure for table mhs.insurancecompany
DROP TABLE IF EXISTS `insurancecompany`;
CREATE TABLE `insurancecompany` (
  `Ins_id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `Street` varchar(50) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `State` varchar(50) DEFAULT NULL,
  `Zip` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Ins_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping structure for table mhs.patient
DROP TABLE IF EXISTS `patient`;
CREATE TABLE `patient` (
  `P_id` int(11) NOT NULL AUTO_INCREMENT,
  `FName` varchar(50) DEFAULT NULL,
  `Minit` varchar(50) DEFAULT NULL,
  `LName` varchar(50) DEFAULT NULL,
  `Street` varchar(50) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `State` varchar(50) DEFAULT NULL,
  `Zip` varchar(50) DEFAULT NULL,
  `Ins_id` int(11) DEFAULT NULL,
  `PrimaryDoctorID` int(11) DEFAULT NULL,
  PRIMARY KEY (`P_id`),
  KEY `FK_patient_doctor` (`PrimaryDoctorID`),
  KEY `FK_patient_insurancecompany` (`Ins_id`),
  CONSTRAINT `FK_patient_doctor` FOREIGN KEY (`PrimaryDoctorID`) REFERENCES `doctor` (`EmpID`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `FK_patient_insurancecompany` FOREIGN KEY (`Ins_id`) REFERENCES `insurancecompany` (`Ins_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping structure for table mhs.doctortreatspatient
DROP TABLE IF EXISTS `doctortreatspatient`;
CREATE TABLE `doctortreatspatient` (
  `Doctor_ID` int(11) NOT NULL,
  `P_id` int(11) NOT NULL,
  PRIMARY KEY (`Doctor_ID`,`P_id`) USING BTREE,
  KEY `FK_doctortreatspatient_patient` (`P_id`),
  CONSTRAINT `FK_doctortreatspatient_doctor` FOREIGN KEY (`Doctor_ID`) REFERENCES `doctor` (`EmpID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_doctortreatspatient_patient` FOREIGN KEY (`P_id`) REFERENCES `patient` (`P_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping structure for table mhs.facility
DROP TABLE IF EXISTS `facility`;
CREATE TABLE `facility` (
  `FaclD` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `State` varchar(50) DEFAULT NULL,
  `Zip` varchar(50) DEFAULT NULL,
  `Size` int(11) DEFAULT NULL,
  `FType` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`FaclD`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping structure for table mhs.office
DROP TABLE IF EXISTS `office`;
CREATE TABLE `office` (
  `FacID` int(11) NOT NULL,
  `Office_Count` int(11) DEFAULT NULL,
  PRIMARY KEY (`FacID`),
  CONSTRAINT `FK_office_facility` FOREIGN KEY (`FacID`) REFERENCES `facility` (`FaclD`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping structure for table mhs.ops
DROP TABLE IF EXISTS `ops`;
CREATE TABLE `ops` (
  `FacID` int(11) NOT NULL,
  `Room_Count` int(11) DEFAULT NULL,
  `P_code` varchar(50) DEFAULT NULL,
  `Description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`FacID`),
  CONSTRAINT `FK_ops_facility` FOREIGN KEY (`FacID`) REFERENCES `facility` (`FaclD`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping structure for table mhs.invoice
DROP TABLE IF EXISTS `invoice`;
CREATE TABLE `invoice` (
  `InvID` int(11) NOT NULL AUTO_INCREMENT,
  `Inv_Date` date DEFAULT NULL,
  `InsuranceID` int(11) DEFAULT NULL,
  `Inv_Amount` decimal(20,2) DEFAULT NULL,
  PRIMARY KEY (`InvID`),
  KEY `FK_invoice_insurancecompany` (`InsuranceID`),
  CONSTRAINT `FK_invoice_insurancecompany` FOREIGN KEY (`InsuranceID`) REFERENCES `insurancecompany` (`Ins_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Data exporting was unselected.

-- Dumping structure for table mhs.makesappointment
DROP TABLE IF EXISTS `makesappointment`;
CREATE TABLE `makesappointment` (
  `Doctor_ID` int(11) NOT NULL,
  `P_id` int(11) NOT NULL,
  `Date_Time` datetime NOT NULL,
  `FaclD` int(11) NOT NULL,
  `InvID` int(11) DEFAULT NULL,
  `Cost` decimal(20,2) DEFAULT NULL,
  `Description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Doctor_ID`,`P_id`,`Date_Time`,`FaclD`),
  KEY `FK_makesappointment_facility` (`FaclD`),
  KEY `FK_makesappointment_invoice` (`InvID`),
  KEY `FK_makesappointment_patient` (`P_id`),
  CONSTRAINT `FK_makesappointment_doctor` FOREIGN KEY (`Doctor_ID`) REFERENCES `doctor` (`EmpID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_makesappointment_facility` FOREIGN KEY (`FaclD`) REFERENCES `facility` (`FaclD`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_makesappointment_invoice` FOREIGN KEY (`InvID`) REFERENCES `invoice` (`InvID`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `FK_makesappointment_patient` FOREIGN KEY (`P_id`) REFERENCES `patient` (`P_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
