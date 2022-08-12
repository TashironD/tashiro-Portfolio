// CSRF対策
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"


document.addEventListener('DOMContentLoaded', function () {

    //varは変数の宣言
    var calendarEl = document.getElementById('calendar');//このjsの指定先　id=calendar

    var calendar = new FullCalendar.Calendar(calendarEl, {
        //表示の設定
        initialView: 'dayGridMonth',
        //日本語
        locale:'ja',
        //月曜日が先頭
        //firstDay:1,

        events: function (info, successCallback, failureCallback) {
            axios
                .post("get_event/", {//get_event関数を実行
                    start_date: info.start.valueOf(),//start_dateの情報を取る
                    end_date: info.end.valueOf(),//end_dateの情報を取る
                })
                .then((response) => {
                    calendar.removeAllEvents();//calendar情報を全削除
                    successCallback(response.data);//取ってきたdate情報をcalendarに表示
                })
                .catch(() => {//失敗したら
                    // バリデーションエラーなど
                    alert("表示に失敗しました");
                });
        },
    });

    calendar.render();//変数calendarを画面に表示
});