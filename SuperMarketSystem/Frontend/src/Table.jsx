import React, { useState, useEffect } from 'react'


export default function Table() {
  const [user, setUser] = useState([])

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/v1/marketSystem/")
    .then(response => response.json())
    .then((data)=> {setUser(data)})
    .catch(err=> console.error(err))
  }, [])

  return (
    <>
      <h1 className="text-center">Super Market System</h1>

      <table className="table table-bordered table-dark">
        <thead>
          <tr>
            <th>Customer Name</th>
            <th>Product One</th>
            <th>Product Two</th>
            <th>Total Price</th>
            <th>Phone No</th>
            <th>Loyalty Points</th>
          </tr>
        </thead>

        <tbody>
          {user.map((value, index) => (
            <tr key={index}>
              <td>{value.customerName}</td>
              <td>{value.productOne}</td>
              <td>{value.productTwo}</td>
              <td>{value.totalPrice}</td>
              <td>{value.phoneNo}</td>
              <td>{value.loyaltyPoints}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  )
}