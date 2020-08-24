const assert = await import("assert");

const wdio = await import("webdriverio");

const opts = {
    port: 4723,
    path: "/wd/hub",
    capabilities: {
        platformName: "android",
        deviceName: "<your-device-name>",
        app: "<your-apk-location>",
        automationName: "UiAutomator2",
        appWaitForLaunch: false
    }
};




describe("Chronology element is visible", function () {

    let client;

    beforeEach(async function () {
        client = await wdio.remote(opts);
    });

    afterEach(async function () {
        await client.deleteSession();
    });


    it("cronology element is visible", async function () {
        await client.pause(10000);
        const xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]";
        const field = await client.$(xpath);
        const visible = await field.isDisplayed();
        assert(visible);


    });
});


describe("navbar is visible", function () {

    let client;

    beforeEach(async function () {
        client = await wdio.remote(opts);
    });

    afterEach(async function () {
        await client.deleteSession();
    });


    it("navbar element is visible", async function () {
        await client.pause(10000);
        const xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup";
        const field = await client.$(xpath);
        const visible = await field.isDisplayed();
        assert(visible);


    });
});

describe("Navigation to patient list works", function () {


    let client;

    beforeEach(async function () {
        client = await wdio.remote(opts);
    });

    afterEach(async function () {
        await client.deleteSession();
    });


    it("navigation test", async function () {
        await client.pause(5000);
        const xpathButton = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]";
        const xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[1]";

        const button = await client.$(xpathButton);

        button.click();

        await client.pause(5000);

        const field = await client.$(xpath);
        const text = await field.getText();

        assert.equal(text, "Os Meus Pacientes");


    });
});


describe("check patient info", function () {


    let client;

    beforeEach(async function () {
        client = await wdio.remote(opts);
    });

    afterEach(async function () {
        await client.deleteSession();
    });


    it("mobile info test", async function () {
        await client.pause(5000);
        const xpathButton1 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]";
        const xpathButton2 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]";
        const button1 = await client.$(xpathButton1);
        button1.click();
        await client.pause(5000);
        const button2 = await client.$(xpathButton2);
        button2.click();
        await client.pause(5000);

        const mobile = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[3]";
        const phone_number = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]";
        const mobile_text = await client.$(mobile);
        const text_mobile = await mobile_text.getText();
        const mobile_number = await client.$(phone_number);
        const text_number = await mobile_number.isDisplayed();
    
        assert(text_number);

        assert.equal(text_mobile, "Mobile");



    });
});


describe("submit treatment", function () {


    let client;

    beforeEach(async function () {
        client = await wdio.remote(opts);
    });

    afterEach(async function () {
        await client.deleteSession();
    });


    it("straight to the end", async function () {
        await client.pause(5000);
        const xpathButton1 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]";
        const xpathButton2 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]";
        const xPathButton3 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup[2]";
        const button1 = await client.$(xpathButton1);
        button1.click();
        await client.pause(5000);
        const button2 = await client.$(xpathButton2);
        button2.click();
        await client.pause(5000);
        
        const button3 = await client.$(xPathButton3);
        button3.click();
        await client.pause(5000);

        /*const treatment = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[1]";
        const treatment_text = await client.$(treatment);
        const actual_treatment_text = await treatment_text.getText();

        assert.equal(actual_treatment_text, "Treatment");
        */

        const anotbutt = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup";
        const anotbutton = await client.$(anotbutt);
        anotbutton.click();
        await client.pause(5000);

        const concluibutt = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[4]";
        const concluibutton = await client.$(concluibutt);
        const concluitest = await concluibutton.isDisplayed();
    
        assert(concluitest);
    

    });
});