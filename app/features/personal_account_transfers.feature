Feature: Account transfers


 Scenario: User is not able to receive incoming transfer when amount is incorresct  
   Given I create personal account with name: "Jan", surname: "Kowalski", pesel: "17594942759"
   When I receive incoming transfer for amount: "100" for account with pesel: "17594942759"
   When I receive incoming transfer for amount: "-100" for account with pesel: "17594942759"
   When Account saldo with pesel: "17594942759" equals: "100"

 Scenario: User is able to receive incoming transfers  
   When I receive incoming transfer for amount: "100" for account with pesel: "17594942759"
   When Account saldo with pesel: "17594942759" equals: "200"


 Scenario: User is able to send outgoing transfer  
   When I send outgoing transfer for amount: "90" with account with pesel: "17594942759"
   When Account saldo with pesel: "17594942759" equals: "110"
   
 Scenario: User is not able to send outgoing transfer when amount in incorresct  
   When I send outgoing transfer for amount: "-90" with account with pesel: "17594942759"
   When Account saldo with pesel: "17594942759" equals: "110"
   
 Scenario: User is not able to send outgoing transfer when amount is greater than saldo  
   When I send outgoing transfer for amount: "120" with account with pesel: "17594942759"
   When Account saldo with pesel: "17594942759" equals: "110"
   
 Scenario: User is able to send series of transfers  
   When I receive incoming transfer for amount: "100" for account with pesel: "17594942759"
   When I receive incoming transfer for amount: "75" for account with pesel: "17594942759"
   When I send outgoing transfer for amount: "50" with account with pesel: "17594942759"
   When Account saldo with pesel: "17594942759" equals: "235"

 Scenario: cleanup
   When I delete account with pesel: "17594942759"