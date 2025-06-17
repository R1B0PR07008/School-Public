// swift-tools-version: 6.0
// The swift-tools-version declares the minimum version of Swift required to build this package.

import Foundation

func get_transaction() {
    let url = URL(string: "https://sandbox.api.mastercard.com/openbanking/connect/api/accounts/account/transactions")
    /// change the URL to production URL when app goes live!!!!
    
    // Request body, hearder and other settings
    var request = URLRequest(url: url!)
    request.httpMethod = "POST"
    
    request.setValue("", forHTTPHeaderField: "")
    
    let body : [String: Any] = [
        "requestInfo": [
            "xRequestId": "123e4567-e89b-12d3-a456-426655440000",
            "consentId": "GFiTpF3:EBy5xGqQMatk",
            "aspspId": "420e5cff-0e2a-4156-991a-f6eeef0478cf",
            "isLivePsuRequest": true,
            "psuTppCustomerId": "420e5cff-0e2a-4156-991a-f6eeef0478cf",
            "psuIPAddress": "192.168.0.1",
            "psuAgent": "PostmanRuntime/7.20.1",
            "merchant": [
                "id": "MerchantId",
                "name": "MerchantName"
            ]
            ],
            "accountId": "aa:q648383844dhhfHhTV",
            "limit": 20,
            "offset": "ofset4prev$earch12345",
            "bookingDateFrom": "2018-11-21",
            "bookingDateTo": "2018-11-23"
    ]
    
    request.httpBody = try? JSONSerialization.data(withJSONObject: body, options: .fragmentsAllowed)
    
    // make the actual request
        
    let task = URLSession.shared.dataTask(with: request) { data, _, error in
        guard let data = data , error == nil else {
            return
        }
        
        do {
            let responce = try  JSONSerialization.jsonObject(with: data, options: .allowFragments)
            print("Response: \(responce) (SUCCES)")
        }
        catch {
            print("Error: \(error) (ERROR)")
        }
    }
    
    task.resume()
}


