//
//  Dash.swift
//  EEz
//
//  Created by Matias Riboldi on 26/10/2024.
//

import SwiftUI

var number = 2000

// MyFuckingGreen = (red: 0.34901, green: 0.7803921, blue: 0.635294)
// My white = red: 238/255, green: 240/255, blue: 251/255
// My black = red: 46/255, green: 40/255, blue: 42/255

struct Dash: View {
    var body: some View {
        NavigationView() {
            VStack {
                RoundedRectangle(cornerRadius: CGFloat(20))
                    .foregroundColor(Color(red: 0.34901, green: 0.7803921, blue: 0.635294))
                    .padding([Edge.Set.horizontal], 20)
                    .padding([Edge.Set.top], 20)
                    .frame(width: 400, height: 200)
                
                NavigationLink(destination: Rojo()) {
                    RoundedRectangle(cornerRadius: CGFloat(20))
                        .foregroundColor(Color.red)
                        .padding([Edge.Set.horizontal], 20)
                        .padding([Edge.Set.top], 20)
                        .frame(width: 400, height: 200)
                        .overlay(
                            Text("You have spent \(number) so far this month \nTo see more info click this square")
                                .foregroundColor(Color.black)
                        )
                }
                
                RoundedRectangle(cornerRadius: CGFloat(20))
                    .foregroundColor(Color.green)
                    .padding([Edge.Set.horizontal], 20)
                    .padding([Edge.Set.top], 20)
                    .frame(width: 400, height: 200)
                    .overlay (
                    Text("Hello, how are you \nIm great \(number)")
                        .foregroundColor(Color(red: 46/255, green: 40/255, blue: 42/255))
                    )
            }
        }
        .navigationTitle("Dash")
        .background(Rectangle()).foregroundColor(Color(red: 238/255, green: 240/255, blue: 251/255))
    }
}

struct Dash_Previews: PreviewProvider {
    static var previews: some View {
        Dash()
    }
}
