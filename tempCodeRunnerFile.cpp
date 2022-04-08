int y) {
//     int posX, posY;
//     queue<int[]> q;
//     q.push({x,y});
//     while(q.size() != 0) {
//         posX = q.front()[0];
//         posY = q.front()[1];
//         q.pop();
//         arr[posY][posX] = 0;
//         if(posX != 0 && arr[posY][posX-1] == 1) q.push({posX-1, posY});
//         if(posX != M-1 && arr[posY][posX+1] == 1) q.push({posX+1, posY});
//         if(posY != 0 && arr[posY-1][posX] == 1) q.push({posX, posY-1});
//         if(posY != N-1 && arr[posY+1][posX] == 1) q.push({posX, posY+1});
//     }
// }