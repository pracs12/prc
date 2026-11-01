pragma solidity ^0.8.18;

contract studentMgmt
{
        struct Student
        {
            uint id;
            string name;
            uint age;
        }

        Student[] public students;

        event addedStudent(uint id,string name,uint age);

        function addStudent(uint _id,string memory _name,uint _age)
        {
            Student memory newStudent = Student({
                id:_id,
                name:_name,
                age:_age
            });

            students.push(newStudent);

            emit addedStudent(_id,_name,_age);

        }


        function getStudents(uint index) public view returns(uint,string memory,uint)
        {
            require(index < students.length,"Student not found");
            Student memory ob = students[index];

            return (ob.id,ob.name,ob.age);
        }

        fallback() external
        {

        }
}