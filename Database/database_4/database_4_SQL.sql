CREATE DATABASE database_4;
USE database_4;

CREATE TABLE PetOwners(
	ownerID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    contact VARCHAR(20)
);

CREATE TABLE Pets(
	petID INT AUTO_INCREMENT PRIMARY KEY,
    ownerID INT,
    FOREIGN KEY (ownerID) REFERENCES PetOwners(ownerID),
    name VARCHAR(20),
    species VARCHAR(20),
    breed VARCHAR(20)
);

CREATE TABLE Rooms(
    roomID INT AUTO_INCREMENT PRIMARY KEY,
    roomNumber CHAR(4),
	roomType VARCHAR(20),
    pricePerNight INT
);

CREATE TABLE Reservations(
	reservationID INT AUTO_INCREMENT PRIMARY KEY,
    petID INT,
    FOREIGN KEY (petID) REFERENCES Pets(petID), 
    roomID INT,
    FOREIGN KEY (roomID) REFERENCES Rooms(roomID),
    startDate DATE,
    endDate DATE
);

CREATE TABLE Services(
	serviceID INT AUTO_INCREMENT PRIMARY KEY,
    reservationID INT,
    FOREIGN KEY (reservationID) REFERENCES Reservations(reservationID),
    serviceName VARCHAR(20),
    servicePrice INT
);


    
