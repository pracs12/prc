// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract StudentMgmt {

    // Structure to store student details
    struct Student {
        uint id;
        string name;
        uint age;
    }

    // Array to store multiple students
    Student[] public students;

    // Event to record student addition
    event addedStudent(uint id, string name, uint age);

    // Function to add a student
    function addStudent(
        uint _id,
        string memory _name,
        uint _age
    ) public {
        Student memory newStudent = Student({
            id: _id,
            name: _name,
            age: _age
        });

        students.push(newStudent);

        emit addedStudent(_id, _name, _age);
    }

    // Function to retrieve student details
    function getStudents(uint index)
        public
        view
        returns (uint, string memory, uint)
    {
        require(index < students.length, "Student not found");

        Student memory ob = students[index];

        return (ob.id, ob.name, ob.age);
    }

    // Fallback function
    fallback() external {
    }
}