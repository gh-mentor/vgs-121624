
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PayrollLibrary
{
    public class Payroll
    {
        /// <summary>
        /// Processes the employees of a given company by iterating through each department
        /// and printing the payment details of each employee.
        /// </summary>
        /// <param name="company">The company whose employees are to be processed.</param>
        public void ProcessEmployees(Company company)
        {
            foreach (var department in company.Departments)
            {
                foreach (var employee in department.Employees)
                {
                    // print the employee payment
                    Console.WriteLine($"{employee.EmployeeDetails}, Payment: {employee.Payment}");
                    
                }
            }
        }
    }
}
